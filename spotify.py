#!/usr/bin/env python


# OS

class NotificationListener(object):
    def __init__(self, notificationName, callback):
        self.notificationName = notificationName
        self.callback = callback

        from Foundation import NSDistributedNotificationCenter
        nc = NSDistributedNotificationCenter.defaultCenter()
        nc.addObserver_selector_name_object_(self, 'callback:', notificationName, None)

    def callback_(self, notification):
        self.callback(notification.object.self)


def wait(time):
    from Foundation import NSDate
    from Foundation import NSRunLoop
    NSRunLoop.mainRunLoop().runBeforeDate_(NSDate.dateWithTimeIntervalSinceNow_(time))


def loop():
    from Foundation import NSRunLoop
    NSRunLoop.mainRunLoop().run()


# Spotify

def onTrackChange(obj):
    import json
    print json.dumps(dict(obj.userInfo()), indent=4, sort_keys=True)


def listen():
    NotificationListener('com.spotify.client.PlaybackStateChanged', onTrackChange)
    while True:
        wait(0.1)


# Program

def main(cmd, *args):
    listen()

class ProgramError(Exception):
    pass

def run():
    from sys import argv, stderr
    try:
        main(*argv)
    except ProgramError, exc:
        print >> stderr, exc
    except KeyboardInterrupt:
        exit(1)

if __name__ == '__main__':
    run()
