from manim import *

config.transparent = True
config.frame_width = 20

Mobject.set_default(
    color='#bbb',
)
Text.set_default(
    font='Linux Libertine Display',
    weight='BOLD',   
    color='#bbb',
)
        
class ImplyIBE(Scene):
    def construct(self):
        ibe = Text('IBE').to_corner(UP)
        self.play(Write(ibe))
        
        enc = Text('Encryption').next_to(ibe, 4*DOWN+LEFT)
        enca = Arrow(ibe, enc.get_top())
        self.play(
            Create(enca),
            Write(enc),
        )
        self.wait()
        
        sig = Text('Signature').next_to(ibe, 4*DOWN+RIGHT)
        siga = Arrow(ibe, sig.get_top())
        self.play(
            Create(siga),
            Write(sig),
        )
        self.wait(10)
        
class ImplyDE(Scene):
    def construct(self):
        de = Text('Delay Encryption').to_corner(UP).shift(LEFT)
        self.play(Write(de))
        
        tlp = Text('Time lock puzzle').next_to(de, 4*DOWN).shift(3*LEFT)
        tlpa = Arrow(de, tlp.get_top())
        self.play(
            Create(tlpa),
            Write(tlp),
        )
        self.wait()
        
        pow = Text('Proof of Work').next_to(de, 4*DOWN).shift(3*RIGHT)
        powa = Arrow(de, pow.get_top())
        self.play(
            Create(powa),
            Write(pow),
        )
        self.wait()

        vdf = Text('/ VDF').next_to(pow, DOWN)
        self.play(
            Write(vdf),
        )
        self.wait(10)
