import aiohttp

__VERSION__ = "0.0.1"
__AUTHOR__ = "Blank-c"

class Life:    
    def __init__(self, proxy: bool= False):
        self.__proxy = proxy
        self._endpoints = ["eight_ball", "cat", "fact", "img_smug", "img_woof", "img_gasm", "img_8ball", "img_goose", "img_avatar", "img_slap", "img_pat", "img_gecg", "img_feed", "fox_girl", "img_lizard",  "img_neko", "img_hug", "img_meow", "img_kiss", "img_wallpaper", "img_tickle", "img_spank", "img_waifu", "img_lewd", "img_ngif", "name", "owoify", "spoiler", "why"]
    
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        return "(Neko's Life)"
        
    def __geturl(self, endpoint):
        url = "https://www.nekos.life/api/v2/" + endpoint
        if self.__proxy:
            return "http://raspe.id.au/bypass/miniProxy.php?" + url
        else:
            return url
            
    async def __sendrequest(self, endpoint):
        url = self.__geturl(endpoint)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                return data

    async def eight_ball(self):
        return await self.__sendrequest("8ball")
        
    async def cat(self):
        return await self.__sendrequest("cat")
        
    async def fact(self):
        return await self.__sendrequest("fact")
        
    async def img_smug(self):
        return await self.__sendrequest("img/smug")
        
    async def img_woof(self):
        return await self.__sendrequest("img/woof")
        
    async def img_gasm(self):
        return await self.__sendrequest("img/gasm")
        
    async def img_8ball(self):
        return await self.__sendrequest("img/8ball")
        
    async def img_goose(self):
        return await self.__sendrequest("img/cuddle")
        
    async def img_avatar(self):
        return await self.__sendrequest("img/avatar")
        
    async def img_slap(self):
        return await self.__sendrequest("img/slap")
        
    async def img_pat(self):
        return await self.__sendrequest("img/pat")
        
    async def img_gecg(self):
        return await self.__sendrequest("img/gecg")
        
    async def img_feed(self):
        return await self.__sendrequest("img/feed")
        
    async def img_fox_girl(self):
        return await self.__sendrequest("img/fox_girl")
        
    async def img_lizard(self):
        return await self.__sendrequest("img/lizard")
        
    async def img_neko(self):
        return await self.__sendrequest("img/neko")
        
    async def img_hug(self):
        return await self.__sendrequest("img/hug")
        
    async def img_meow(self):
        return await self.__sendrequest("img/meow")
        
    async def img_kiss(self):
        return await self.__sendrequest("img/kiss")
        
    async def img_wallpaper(self):
        return await self.__sendrequest("img/wallpaper")
        
    async def img_tickle(self):
        return await self.__sendrequest("img/tickle")
        
    async def img_spank(self):
        return await self.__sendrequest("img/spank")
        
    async def img_waifu(self):
        return await self.__sendrequest("img/waifu")
        
    async def img_lewd(self):
        return await self.__sendrequest("img/lewd")
        
    async def img_ngif(self):
        return await self.__sendrequest("img/ngif")
        
    async def name(self):
        return await self.__sendrequest("name")
        
    async def owoify(self, text):
        return await self.__sendrequest("owoify?text=" + text)
        
    async def spoiler(self, text):
        return await self.__sendrequest("spoiler?text=" + text)

    async def why(self):
        return await self.__sendrequest("why")
