from Class_TextChat import*

if __name__ == "__main__":
    print('Running TCP server')
    sev=TextChat('Server')
    sev.win.mainloop()