from customtkinter import *

code = {
    "a" : "1",
    "b" : "2",
    "c" : "3",
    "d" : "4",
    "e" : "5",
    "f" : "6",
    "g" : "7",
    "h" : "8",
    "i" : "9",
    "j" : "10",
    "k" : "11",
    "l" : "12",
    "m" : "13",
    "n" : "14",
    "o" : "15",
    "p" : "16",
    "q" : "17",
    "r" : "18",
    "s" : "19",
    "t" : "20",
    "u" : "21",
    "v" : "22",
    "w" : "23",
    "x" : "24",
    "y" : "25",
    "z" : "26"
}


def coder():
    global operator_l
    for i in entry_text_left.get():
        for k, v in code.items():
            if i == k:
                operator_l = operator_l + v
                operator_l = operator_l + " "
    coder_.set(operator_l)
    operator_l = ""


def decoder():
    global operator_r
    final_ = entry_code_right.get().split(" ")
    for i in final_:
        for k, v in code.items():
            if i == v:
                operator_r = operator_r + k
    decoder_.set(operator_r)
    operator_r = ""


set_appearance_mode("dark")
set_default_color_theme("blue")

title_font = ("Comic Sans MS", 20, "bold")
label_font = ("Comic Sans MS", 18, "bold")
entry_font = ("Comic Sans MS", 16, "bold")

root = CTk()
root.title("Coder / Decoder")
root.geometry("900x506")
coder_ = StringVar()
decoder_ = StringVar()
operator_r = ""
operator_l = ""


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

frame_coder = CTkFrame(root, corner_radius=20, fg_color="#1f2937")

frame_coder.grid(row=0, column=0, padx=(40, 15), pady=70, sticky="nsew")
frame_coder.grid_columnconfigure(0, weight=1)

label_coder = CTkLabel(frame_coder, text="Coder", font=title_font, text_color="#60a5fa")
label_coder.grid(row=0, column=0, pady=(25, 30))

label_text_left = CTkLabel(frame_coder, text="Text", font=label_font)
label_text_left.grid(row=1, column=0, pady=(0, 8))

entry_text_left = CTkEntry(frame_coder, width=280, height=40, font=entry_font, justify="center", placeholder_text="Enter name")
entry_text_left.grid(row=2, column=0, padx=30, pady=(0, 20))


label_code_left = CTkLabel(frame_coder, text="Code", font=label_font)
label_code_left.grid(row=3, column=0, pady=(0, 8))

entry_code_left = CTkEntry(frame_coder, font=entry_font, justify="center", width=280, height=40, textvariable=coder_)
entry_code_left.grid(row=4, column=0, padx=30, pady=(0, 25))

btn_code_left = CTkButton(frame_coder, text="Code", font=label_font, width=180, height=42, command=coder)
btn_code_left.grid(row=5, column=0, pady=(0, 25))

#=======================================================================================================================

frame_decoder = CTkFrame(root, corner_radius=20, fg_color="#1f2937")

frame_decoder.grid(row=0, column=1, padx=(40, 15), pady=70, sticky="nsew")
frame_decoder.grid_columnconfigure(1, weight=1)

label_coder = CTkLabel(frame_decoder, text="DeCoder", font=title_font, text_color="#60a5fa")
label_coder.grid(row=0, column=1, pady=(25, 30))

label_text_right = CTkLabel(frame_decoder, text="Text", font=label_font)
label_text_right.grid(row=3, column=1, pady=(0, 8))

entry_text_right = CTkEntry(frame_decoder, width=280, height=40, font=entry_font, justify="center", textvariable=decoder_)
entry_text_right.grid(row=4, column=1, padx=30, pady=(0, 20))


label_code_right = CTkLabel(frame_decoder, text="Code", font=label_font)
label_code_right.grid(row=1, column=1, pady=(0, 8))

entry_code_right = CTkEntry(frame_decoder, font=entry_font, justify="center", width=280, height=40, placeholder_text="Enter code")
entry_code_right.grid(row=2, column=1, padx=30, pady=(0, 25))

btn_code_right= CTkButton(frame_decoder, text="Text", font=label_font, width=180, height=42, command=decoder)
btn_code_right.grid(row=5, column=1, pady=(0, 25))

root.mainloop()