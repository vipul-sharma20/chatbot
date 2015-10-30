import aiml


class Bot():
    def connect(self):
        k = aiml.Kernel()
        print k.learn('std-startup.xml')
        print k.respond('LOAD AIML B')
        return k
    def message(self, ker, message):
        rep = k.respond(message)
        return rep

