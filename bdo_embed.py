import discord
from Error import *

class BDOembed(object):
    def __init__(self, message, title, description, colour=0, field=[], fielddesc=[], image=None):
        """
        BDOembed object
        :param message: message Message object created when command is called
        :param title: str Title string used for embed
        :param description: str Description used for embed
        :param colour: Colour/int Discord Colour value or number specifying color of embed
        :param field: list List of field titles used for embed
        :param fielddesc: list List of field descriptions used for embed
        :param image: str Path/name of image file used for embed
        :return: N/A
        """
        self.message = message
        self.title = title
        self.description = description
        self.colour = colour
        self.embed = discord.Embed(
            title = self.title,
            description = self.description,
            colour = discord.Colour(colour)
        )

        # Error check field is list in case some bozo inputs something else
        if type(field) is not list or type(fielddesc) is not list:
            raise TypeError('field/fielddesc must be of type list.')
        # Error check field and fielddesc are the same length
        if len(field) != len(fielddesc):
            raise LengthError('field and fielddesc must be same length.')

        self.field = field
        self.fielddesc = fielddesc

        # Add fields to embedded message
        for i in range(len(field)):
            self.embed.add_field(name=field[i], value=fielddesc[i], inline=False)

        self.image = image

        # Add image to embedded message
        self.imagefile = discord.File(image, filename="image.jpg")
        self.embed.set_image(url="attachment://image.jpg")

    async def sendMessage(self):
        """
        Send embedded message to user's channel
        """
        await self.message.channel.send(file=self.imagefile, embed=self.embed)

    def testFunction(self):
        print()
