from manim import *
import random, math

config.transparent = True
config.frame_width = 30

Mobject.set_default(
    color='#bbb',
)
Dot.set_default(
    color='#bbb',
)
Line.set_default(
    color='#bbb',
)
Text.set_default(
    font='Linux Libertine Display',
    weight='BOLD',   
    color='#bbb',
)
        
class Walk(Scene):
    def construct(self):
        j0 = Dot(radius=.2)
        j0t = Text('1728').next_to(j0, DOWN)
        self.play(
            Create(j0),
            Write(j0t)
        )
        self.wait()

        random.seed(0)

        pp = PolarPlane()

        for n in range(3):
            js = VGroup(j0)
            for i in range(100):
                p = (30,0,0)
                while (abs(p[0]) > 8 or abs(p[1]) > 5):
                    p = js[-1].get_center() + pp.pr2pt(2, random.random()*2*math.pi)
                j = Dot().move_to(p)
                l = Line(js[-1], j)
                js.add(l, j)

            self.play(Create(js))
        
            j0 = Dot(radius=.2).move_to(js[-1])
            j0t = Text('E' + chr(ord('₀')+n)).next_to(j0,
                                                      pp.pr2pt(-1, pp.pt2pr(j0.get_center())[1]))
            self.play(
                Create(j0),
                Write(j0t),
            )
            self.wait()

            self.play(
                FadeOut(js[1:]),
            )
            self.wait()

        self.play(Create(Dot(radius=.2).move_to([-3,2,0])))
        self.play(Create(Dot(radius=.2).move_to([-1,4,0])))
        self.play(Create(Dot(radius=.2).move_to([3,-1.5,0])))

        jend = Dot(radius=.2).move_to([-3.3,-1.7,0])
        jendt = MarkupText('E<sub>n</sub>').next_to(jend, DOWN)
        self.play(
            Create(jend),
            Write(jendt),
        )
        self.play(
            VGroup(jend, jendt).animate.scale(2).set_fill(RED),
        )
            
        self.wait(20)
