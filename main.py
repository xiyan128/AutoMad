from lib import MadDump

if __name__ == '__main__':
    dump = MadDump("input1.mp4", "input2.mp4", audio="test.mp3")
    dump.find_all_scenes()
    dump.export("out.mp4")
