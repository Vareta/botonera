import os

from aiohttp import web
from sounds import library

def get_content_type(path):
    types = {
        'wav': 'audio/x-wav',
        'mp3': 'audio/mpeg'
    }
    extension = path.split('.')[-1]
    try:
        return types[extension]
    except KeyError as _:
        return None

async def get_audio_file(request):
    name = request.match_info.get('name', None)
    if name:
        try:
            sound_path = library[name]['path']
            response = web.StreamResponse()
            response.content_type = get_content_type(sound_path)
            response.content_length = os.stat(sound_path).st_size
            await response.prepare(request)
            with open(sound_path, 'rb') as f:
                await response.write(f.read())
            return response
        except KeyError as _:
            return web.Response(text='no encontrado', status=404)
    else:
        return web.Response(text='sin información', status=400)

app = web.Application()
app.add_routes([web.get('/{name}', get_audio_file)])
web.run_app(app)