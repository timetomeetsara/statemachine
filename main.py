import string
from state import State
# A different subclass for each state:

class Critical(State):
    def run(self):
        print("Please seek help inmediatly")


class NoHelp(State):
    def run(self):
        print("Sorry, I can't help you with this")


class Burocrazy(State):
    def run(self):
        print("Sorry, I can't help you with this but I know who can!")
        print("You should check Burocrazy, those guys are cool")


class Initial(State):
    def run(self):
        print("Hi there. My name is Hadi")
        print("I'm here for you. What's up")
        print("A - I feel up")
        print("B - I feel down")
        return raw_input("")

    def next(self, answer):
        if 'up' in answer:
            return FeelUp()
        if 'down' in answer:
            return FeelDown()
        return NoHelp()

class FeelUp(State):
    def run(self):
        print("Great!")
        return raw_input("Would you like to cheer someone up?")

    def next(self, answer):
        if 'y' in answer:
            return Introduce()
        return Oops()

class FeelDown(State):
    def run(self):
        print("So sorry to hear that")
        print("Whats wrong?")
        print("I'm bored")
        print("I'm sad")
        print("I'm stressed with paperwork")
        print("I'm lost")
        print("I'm tired")
        print("I miss my country")
        print("I feel lonely")
        print("I'm angry")
        print("I'm feeling ill")
        print("None of that")
        return raw_input()

    def next(self, answer):
        if "bored" in answer:
            return Bored()
        if "sad" in answer:
            return Sad()
        if "paperwork" in answer:
            return Burocrazy()
        if "stressed" in answer:
            return Burocrazy()
        if "lost" in answer:
            return Lost()
        if "tired" in answer:
            return Tired()
        if "miss" in answer:
            return HomeSick()
        if "country" in answer:
            return HomeSick()
        if "lonely" in answer:
            return Lonely()
        if "angry" in answer:
            return Angry()
        if "ill" in answer:
            return Ill()
        if "None" in answer:
            return NoHelp()

class HotLine(State):
    def run(self):
        print("You need inmediate help!")
        print("Call the emergency hotline")
        print("http://www.suicide.org/hotlines/international/germany-suicide-hotlines.html")
        print("http://www.frauenhauskoordinierung.de/english-summary.html")


class Bored(State):
    def run(self):
        print ("Would you like to meet people with your same interests?")
        print("Yeah, sure!")
        print("Not right now")

    def next(self, answer):
        if 'Yeah' in answer:
            return MeetUp()
        if "Not" in answer:
            return Bored2()

class Bored2(State):
    def run(self):
        print ("What about viewing some funny videos?")
        print("Yes, of course!")
        print("Not really")

    def next(self, answer):
        if 'Yeah' in answer:
            return FunnyVideos()
        if "Not" in answer:
            return Bored3()

class Bored3(State):
    def run(self):
        print ("Do you prefer to go to cinema?")
        print("Yeah, I'd love to!")
        print("Not right now")

    def next(self, answer):
        if 'Yeah' in answer:
            return Cinema()
        if "Not" in answer:
            return Sports()


class FunnyVideos(State):
    def run(self):
        print("Check this web page!")
        print("https://www.youtube.com/results?search_query=funny")


class HeadSpace(State):
    def run(self):
        print ("Try an app like HeadSpace to learn how to meditate")


class Cinema(State):
    def run(self):
        print("Here you can find cinemas around you!")
        print("https://www.google.com/maps?q=cinema")


class Tired(State):
    def run(self):
        print ("Why are you tired?")
        print("I'm mentally exhausted")
        print("I feel my body has no energy")
        return raw_input()

    def next(self, answer):
        if 'mentally' in answer:
            return HeadSpace()
        if 'physcally' in answer:
            return Sleeping()

class Sports(State):
    def run(self):
        print("Here you can find sports events (and more)!")
        print("https://www.sportsworld.co.uk/events")


class Lost(State):
    def run(self):
        print ("What are you looking for?")
        print("I want to go somewhere")
        print("I need help with my paperwork")
        print("Someone to talk to")
        return raw_input()

    def next(self, answer):
        if 'somewhere' in answer:
            return GoogleMaps()
        if 'paperwork' in answer:
            return Burocrazy()
        if 'Someone' in answer:
            return Lonely()

class Ill(State):
    def run(self):
        print ("Look this awesome link to german national health system")

class Lonely(State):
    def run(self):
        print("Would you like to meet new people?")
        print("Yeah, I would like talk with someone")
        print("It would be cool to join some activity")
        print("Not right now")

    def next(self, answer):
        if 'Yeah' in answer:
            return Introduce()
        if "activity" in answer:
            return MeetUp()
        if "Not" in answer:
            return TedTalk()

class MeetUp(State):
    def run(self):
        print("Check MeetUp! You'll find something you like for sure")
        print("http://www.meetup.com/")


class TedTalk(State):
    def run(self):
        print("Watch this inpirational talks on how to deal with feeling lonely")
        print("http://www.keepinspiring.me/25-creative-and-surprising-things-to-do-when-you-feel-lonely/")


class Introduce(State):
    def run(self):
        print("Let me introduce you to my friend Hans!")


class GoogleMaps(State):
    def run(self):
        print("Try searching at GoogleMaps :)")
        print("https://www.google.com/maps")


class HomeSick(State):
    def run(self):
        print("It's hard to be away from home")
        print("Some food would be great")
        print("I would like to find cool things to do around")
        return raw_input("")

    def next(self, answer):
        if 'food' in answer:
            return GoogleMaps()
        if 'things' in answer:
            return MeetUp()

class Oops(State):
    def run(self):
        print("Oops, I'm sorry to hear that")
        print("Talk to me later if you want")



currentState = Initial()

while True:
    if currentState:
        answer = currentState.run()
        currentState = currentState.next(answer)
    else:
        break



