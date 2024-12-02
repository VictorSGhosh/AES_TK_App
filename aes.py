import copy
import tkinter
import tkinter.ttk
from functools import partial
from tkinter import *
from tkinter import ttk

class AES:
    firstrun = True
    S_BOX = (0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
             0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
             0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
             0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
             0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
             0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
             0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
             0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
             0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
             0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
             0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
             0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
             0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
             0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
             0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
             0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,)
    INV_S_BOX = (0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
                 0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
                 0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
                 0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
                 0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
                 0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
                 0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
                 0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
                 0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
                 0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
                 0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
                 0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
                 0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
                 0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
                 0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
                 0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,)
    # ROUND_CONST = [
    #     [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80,
    #      0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A, 0x2F,
    #      0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A, 0xD4],
    #     [0x00]*24,
    #     [0x00]*24,
    #     [0x00]*24
    # ]
    ROUND_CONST = [
        [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D],
        [0x00] * 14, [0x00] * 14, [0x00] * 14
    ]

    nk = 4
    nb = 4
    nr = 10

    def __sub_bytes(self, inp):
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                inp[i][j] = self.S_BOX[inp[i][j]]
        return inp

    def __inv_sub_bytes(self, inp):
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                inp[i][j] = self.INV_S_BOX[inp[i][j]]
        return inp

    def __shift_rows(self, inp):
        for i in range(1, self.nb):
            inp[i] = inp[i][i:] + inp[i][:i]
        return inp
        # inp[1][0], inp[1][1], inp[1][2], inp[1][3] = inp[1][1], inp[1][2], inp[1][3], inp[1][0]
        # inp[2][0], inp[2][1], inp[2][2], inp[2][3] = inp[2][2], inp[2][3], inp[2][0], inp[2][1]
        # inp[3][0], inp[3][1], inp[3][2], inp[3][3] = inp[3][3], inp[3][0], inp[3][1], inp[3][2]

    def __inv_shift_rows(self, inp):
        for i in range(1, self.nb):
            inp[i] = inp[i][len(inp) - i:] + inp[i][:len(inp) - i]
        return inp
        # inp[1][0], inp[1][1], inp[1][2], inp[1][3] = inp[1][3], inp[1][0], inp[1][1], inp[1][2]
        # inp[2][0], inp[2][1], inp[2][2], inp[2][3] = inp[2][2], inp[2][3], inp[2][0], inp[2][1]
        # inp[3][0], inp[3][1], inp[3][2], inp[3][3] = inp[3][1], inp[3][2], inp[3][3], inp[3][0]

    def __mul_02(self, num):
        if num < 0x80:
            res = (num << 1)
        else:
            res = (num << 1) ^ 0x1b
        return res % 0x100

    def __mul_03(self, num):
        return self.__mul_02(num) ^ num

    def __mul_09(self, num):
        return self.__mul_02(self.__mul_02(self.__mul_02(num))) ^ num

    def __mul_0b(self, num):
        return self.__mul_02(self.__mul_02(self.__mul_02(num))) ^ self.__mul_02(num) ^ num

    def __mul_0d(self, num):
        return self.__mul_02(self.__mul_02(self.__mul_02(num))) ^ self.__mul_02(self.__mul_02(num)) ^ num

    def __mul_0e(self, num):
        return self.__mul_02(self.__mul_02(self.__mul_02(num))) ^ self.__mul_02(self.__mul_02(num)) ^ self.__mul_02(num)

    def __mix_columns(self, inp):
        for i in range(self.nb):
            s0 = self.__mul_02(inp[0][i]) ^ self.__mul_03(inp[1][i]) ^ inp[2][i] ^ inp[3][i]
            s1 = inp[0][i] ^ self.__mul_02(inp[1][i]) ^ self.__mul_03(inp[2][i]) ^ inp[3][i]
            s2 = inp[0][i] ^ inp[1][i] ^ self.__mul_02(inp[2][i]) ^ self.__mul_03(inp[3][i])
            s3 = self.__mul_03(inp[0][i]) ^ inp[1][i] ^ inp[2][i] ^ self.__mul_02(inp[3][i])
            inp[0][i] = s0
            inp[1][i] = s1
            inp[2][i] = s2
            inp[3][i] = s3
        return inp

    def __inv_mix_columns(self, inp):
        for i in range(self.nb):
            s0 = self.__mul_0e(inp[0][i]) ^ self.__mul_0b(inp[1][i]) ^ self.__mul_0d(inp[2][i]) ^ self.__mul_09(
                inp[3][i])
            s1 = self.__mul_09(inp[0][i]) ^ self.__mul_0e(inp[1][i]) ^ self.__mul_0b(inp[2][i]) ^ self.__mul_0d(
                inp[3][i])
            s2 = self.__mul_0d(inp[0][i]) ^ self.__mul_09(inp[1][i]) ^ self.__mul_0e(inp[2][i]) ^ self.__mul_0b(
                inp[3][i])
            s3 = self.__mul_0b(inp[0][i]) ^ self.__mul_0d(inp[1][i]) ^ self.__mul_09(inp[2][i]) ^ self.__mul_0e(
                inp[3][i])
            inp[0][i] = s0
            inp[1][i] = s1
            inp[2][i] = s2
            inp[3][i] = s3
        return inp

    def __key_expansion(self, key):
        key_hex = [ord(symbol) for symbol in key]

        for i in range(4 * self.nk - len(key_hex)):
            key_hex.append(0x01)

        key_schedule = [[] for _ in range(4)]
        for r in range(4):
            for c in range(self.nk):
                key_schedule[r].append(key_hex[r + 4 * c])

        for c in range(self.nk, self.nb * (self.nr + 1)):
            if c % self.nk == 0:
                col = [key_schedule[r][c - 1] for r in range(1, 4)]
                col.append(key_schedule[0][c - 1])
                for i in range(len(col)):
                    col[i] = self.S_BOX[16 * (col[i] // 0x10) + (col[i] % 0x10)]
                for r in range(4):
                    s = key_schedule[r][c - 4] ^ col[r] ^ self.ROUND_CONST[r][c // self.nk - 1]
                    key_schedule[r].append(s)
            else:
                for r in range(4):
                    s = key_schedule[r][c - 4] ^ key_schedule[r][c - 1]
                    key_schedule[r].append(s)

        return key_schedule

    def __add_round_key(self, inp, key_schedule, aes_round=0):
        col_shift = self.nb * aes_round
        for c in range(self.nk):
            for r in range(4):
                inp[r][c] = inp[r][c] ^ key_schedule[r][col_shift + c]
        return inp

    def __add_padding(self, plain_text):
        padding_len = 16 - (len(plain_text) % 16)
        padding = ([chr(padding_len)] * padding_len)
        return plain_text + "".join(padding)

    def __remove_padding(self, padded_plain_text):
        padding_len = ord(padded_plain_text[-1])
        assert padding_len > 0
        plain_text, padding = padded_plain_text[:-padding_len], padded_plain_text[-padding_len:]
        assert all(ord(p) == padding_len for p in padding)
        return plain_text

    def __display_first_block(self, heading, prev, text_block):
        rootsub = Tk()
        rootsub.title(heading + " first round")
        w = 315
        h = 220
        ws = rootsub.winfo_screenwidth()  # width of the screen
        hs = rootsub.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        rootsub.geometry('%dx%d+%d+%d' % (w, h, x, y))

        a = Text(rootsub, width=12, height=2, wrap='word')
        a.insert(tkinter.END, "Pre " + heading)
        a.grid(row=0, column=0, columnspan=3)

        b = Text(rootsub, width=12, height=2, wrap='word')
        b.insert(tkinter.END, "Post " + heading)
        b.grid(row=0, column=4, columnspan=3)

        for row in range(1, 5):
            for column in range(9):
                if column == 4:
                    e = Label(rootsub, text='     \n   ', bg='black')
                    e.grid(row=row, column=column)
                    continue
                e = Text(rootsub, width=4, height=2)
                if column > 4:
                    e.insert(tkinter.END, hex(text_block[row - 1][column - 5]))
                else:
                    e.insert(tkinter.END, hex(prev[row - 1][column]))
                e.grid(row=row, column=column)
        b = Button(rootsub, text='Next', command=rootsub.destroy)
        b.grid(row=6, column=3, columnspan=3)
        rootsub.mainloop()

    def store(self, root4, cipher_text):
        f = open("cipher.txt", "w")
        f.write(cipher_text)
        f.close()
        root4.destroy()

    def __encrypt_block(self, plain_text_block, key_schedule):
        text_block = [[] for _ in range(self.nb)]

        for r in range(4):
            for c in range(self.nb):
                text_block[r].append(ord(plain_text_block[r + 4 * c]))

        text_block = self.__add_round_key(text_block, key_schedule)
        for curr_round in range(1, self.nr):
            if (curr_round == 1 and self.firstrun):
                self.firstrun = False
                prev = copy.deepcopy(text_block)
                text_block = self.__sub_bytes(text_block)
                self.__display_first_block("sub-bytes", prev, text_block)

                prev = copy.deepcopy(text_block)
                text_block = self.__shift_rows(text_block)
                self.__display_first_block("shift-rows", prev, text_block)

                prev = copy.deepcopy(text_block)
                text_block = self.__mix_columns(text_block)
                self.__display_first_block("mix-columns", prev, text_block)

                prev = copy.deepcopy(text_block)
                text_block = self.__add_round_key(text_block, key_schedule, curr_round)
                self.__display_first_block("round-key", prev, text_block)
            else:
                text_block = self.__sub_bytes(text_block)
                text_block = self.__shift_rows(text_block)
                text_block = self.__mix_columns(text_block)
                text_block = self.__add_round_key(text_block, key_schedule, curr_round)

        text_block = self.__sub_bytes(text_block)
        text_block = self.__shift_rows(text_block)
        text_block = self.__add_round_key(text_block, key_schedule, self.nr)

        cipher_out = ['' for _ in range(4 * self.nb)]
        for r in range(4):
            for c in range(self.nb):
                cipher_out[r + 4 * c] = chr(text_block[r][c])
        return "".join(cipher_out)

    def encrypt(self, plain_text, key):
        # display the text and key
        root2 = Tk()
        root2.title("Input")
        text_label = ttk.Label(text="Text")
        text_label.pack(fill='x', expand=True)

        ptext = Text(root2, wrap='word', height=5);
        ptext.pack(fill='x', expand=True);
        ptext.insert(tkinter.END, plain_text);

        key_label = ttk.Label(text="Key")
        key_label.pack(fill='x', expand=True)

        ktext = Text(root2, wrap='word', height=5);
        ktext.pack(expand=True);
        ktext.insert(tkinter.END, key);

        Button(root2, text='Next', command=root2.destroy).pack(side='bottom')
        root2.mainloop();

        # get the key matrix

        key_schedule = self.__key_expansion(key)

        # display the key matrix

        print(key_schedule)
        root3 = Tk()
        root3.title("Expanded Key")
        f = Frame(root3)
        f.pack()
        for row in range(len(key_schedule)):
            for column in range(len(key_schedule[0])):
                if column < 4:
                    e = Text(f, width=4, height=2, background="yellow", foreground="black")
                    e.insert(tkinter.END, hex(key_schedule[row][column]))
                    e.grid(row=row, column=column, stick="nsew")
                else:
                    e = Text(f, width=4, height=2)
                    e.insert(tkinter.END, hex(key_schedule[row][column]))
                    e.grid(row=row, column=column, stick="nsew")
        Button(root3, text='Next', command=root3.destroy).pack()
        #b.grid(row=len(key_schedule) + 1, column=int(len(key_schedule[0]) / 2), columnspan=2)
        root3.mainloop()

        # get the padded text

        padded_plain_text = self.__add_padding(plain_text)

        cipher_text = ""
        for i in range(len(padded_plain_text) // 16):
            cipher_text += self.__encrypt_block(padded_plain_text[i * 16: i * 16 + 16], key_schedule)

        # display cipher text
        root4 = Tk()
        root4.title("Cipher Text")

        ctext = Text(root4, wrap='word');
        ctext.pack(expand=True);
        ctext.insert(tkinter.END, cipher_text);
        Button(root4, text='Store', command=partial(
            self.store, root4, cipher_text)).pack()
        Button(root4, text='Next', command=root4.destroy).pack(side='bottom')
        root2.mainloop();
        return cipher_text

    def __decrypt_block(self, cipher_text_block, key_schedule):
        cipher_block = [[] for _ in range(self.nb)]

        for r in range(4):
            for c in range(self.nb):
                cipher_block[r].append(ord(cipher_text_block[r + 4 * c]))

        cipher_block = self.__add_round_key(cipher_block, key_schedule, self.nr)
        curr_round = self.nr - 1
        while curr_round >= 1:
            cipher_block = self.__inv_shift_rows(cipher_block)
            cipher_block = self.__inv_sub_bytes(cipher_block)
            cipher_block = self.__add_round_key(cipher_block, key_schedule, curr_round)
            cipher_block = self.__inv_mix_columns(cipher_block)
            curr_round -= 1

        cipher_block = self.__inv_shift_rows(cipher_block)
        cipher_block = self.__inv_sub_bytes(cipher_block)
        cipher_block = self.__add_round_key(cipher_block, key_schedule, curr_round)

        text_out = ['' for _ in range(4 * self.nb)]
        for r in range(4):
            for c in range(self.nb):
                text_out[r + 4 * c] = chr(cipher_block[r][c])
        return "".join(text_out)

    def decrypt(self, cipher_text, key):
        key_schedule = self.__key_expansion(key)

        padded_plain_text = ""
        for i in range(len(cipher_text) // 16):
            padded_plain_text += self.__decrypt_block(cipher_text[i * 16: i * 16 + 16], key_schedule)

        plain_text = self.__remove_padding(padded_plain_text)

        return plain_text
