from bs4 import BeautifulSoup
import requests


class Spell:
    def __init__(self, name, source, castingType=""):
        self.name = name
        self.source = source
        self.scrapeSpell()

    def scrapeSpell(self):
        url = "http://dnd5e.wikidot.com/spell:" + self.name
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        heading = self.name.replace("-", " ").title()
        heading = soup.find("span", text=heading)

        spells = heading.findNext().findNext().findNext().findChildren()

        sourceBook = spells[1]
        text = spells[12]
        higherLevel = spells[14].next.next.next

        castingInfo = spells[4]
        castingTime = castingInfo.next.next.next
        range = castingTime.next.next.next.next.next
        components = range.next.next.next.next.next
        duration = components.next.next.next.next.next

        self.sourcebook = sourceBook.text
        self.text = text.text
        self.higherLevel = higherLevel.text

        self.castingTime = castingTime.text
        self.range = range.text
        self.components = components.text
        self.duration = duration.text
