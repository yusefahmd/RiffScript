from tabs2music.main import run as tabs2music
from compiler import compiler

# tabs_path: a path to the .txt file containing the tabs input. The name of the file is the song name
# audio_save_path: a path to the directory the .midi and .wav files should be saved to
# soundfont_path: a path to the soundfont file
# save_midi (optional): if True, the .midi file will be saved, otherwise it is deleted
# play_midi (optional): if True, the .midi file will be played via the terminal on creation, otherwise nothing is played
# tempo (optional): measured in bpm, and changing the value from the default 120 will change the speed of the song
# riff_script (optional): should always be set to True, as it is passed to tabs2music, an add-on library that will convert the tabs to a .wav file
def main(tabs_path, audio_save_path, soundfont_path, save_midi=False, play_midi=False, tempo=120, for_riff_script=True):
    # tabs2music will return the tabs_notes so they can be compiled to code, and will generate the .wav file of the code created
    tabs_notes = tabs2music(tabs_path, audio_save_path, soundfont_path, for_riff_script=for_riff_script)

    # Pass the tabs_notes to the RiffScript parser, and to the tabs2music parser
    compiler(tabs_notes) # I think this will have no return

main(r"C:\Users\yusef\Documents\test_tabs2music\tabs.txt.txt", r"C:\Users\yusef\Documents\test_tabs2music", r"C:\Users\yusef\Documents\test_tabs2music\sf.sf2", tempo=200)