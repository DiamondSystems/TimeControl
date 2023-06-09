class Grip:
    ''' Makes a window dragable. '''
    def __init__ (self, parent, disable=None, goingBeyond=True, releasecmd=None) :
        self.parent = parent
        self.root = parent.winfo_toplevel()

        self.disable = disable
        if type(disable) == 'str':
            self.disable = disable.lower()

        self.releaseCMD = releasecmd
        self.goingBeyond = goingBeyond;

        if not self.goingBeyond :
            self.maxX = self.root.winfo_screenwidth() - self.root.winfo_reqwidth()
            self.maxY = self.root.winfo_screenheight() - self.root.winfo_reqheight()

        self.parent.bind('<Button-1>', self.relative_position)
        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.root.geometry().split("+")
        self.oriX, self.oriY = int(geo[1]), int(geo[2])
        self.relX = cx - self.oriX
        self.relY = cy - self.oriY

        self.parent.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        d = self.disable
        x = cx - self.relX
        y = cy - self.relY
    
        if d == 'x' :
            x = self.oriX
        elif d == 'y' :
            y = self.oriY

        if not self.goingBeyond :
            if x < 0 :
                x = 0;
            elif x > self.maxX :
                x = self.maxX
            
            if y < 0 :
                y = 0;
            elif y > self.maxY :
                y = self.maxY
        
        self.root.geometry('+%i+%i' % (x, y))

    def drag_unbind (self, event) :
        self.parent.unbind('<Motion>')
        if self.releaseCMD != None :
            self.releaseCMD()