from manim import *

BCOLOR = '#546953'
config.background_color = BCOLOR
config.frame_width = 30

Text.set_default(
    font='Linux Libertine Display',
)

class IBE(MovingCameraScene):
    def construct(self):
        boxkg = Rectangle(height=1, width=3, fill_opacity=1).move_to((-10,4,0))
        keygen = Text('KeyGen', color=BCOLOR).move_to(boxkg)
        self.play(
            FadeIn(boxkg),
            Write(keygen),
        )
        msk = Text('msk').next_to(boxkg, 3*UP + 7*RIGHT).scale(.8)
        mpk = Text('pk').next_to(boxkg, 3*DOWN + 7*RIGHT).scale(.8)
        arrows = Arrow(boxkg, msk)
        arrowp = Arrow(boxkg, mpk)
        self.play(
            Create(arrows),
            Create(arrowp),
            Write(msk),
            Write(mpk),
        )
        self.wait()

        boxenc = Rectangle(height=1.4, width=5, fill_opacity=1).move_to((0,1,0))
        encrypt = Text('Encrypt', color=BCOLOR).move_to(boxenc)
        self.play(
            FadeIn(boxenc),
            Write(encrypt),
        )
        id = ImageMobject('doge.png').scale(.2).next_to(boxenc, 7*UP)
        idt = Text('id').next_to(id, RIGHT).scale(.8)
        self.play(
            FadeIn(id),
            Write(idt),
        )
        msg = VGroup(
            Rectangle(height=0.5, width=1),
            Line((-0.5, 0.2, 0), ORIGIN),
            Line((0.5, 0.2, 0), ORIGIN),
        ).next_to(boxenc, 14*LEFT)
        msgt = Text('msg').next_to(msg, DOWN).scale(.8)
        self.play(
            Create(msg),
            Write(msgt),
        )
        arrowm = Arrow(msg.get_right(), boxenc.get_left())
        arrowp = Arrow(mpk.get_right(), boxenc)
        arrowi = Arrow(id.get_bottom(), boxenc.get_top())
        self.play(
            Create(arrowm),
            Create(arrowp),
            Create(arrowi),
        )
        ct = Text('ct').next_to(boxenc, 4*RIGHT).scale(.8)
        arrowct = Arrow(boxenc.get_right(), ct.get_left())
        self.play(
            Create(arrowct),
            Write(ct),
        )
        self.wait()

        boxext = Rectangle(height=1, width=3, fill_opacity=1).move_to((0,7,0))
        extract = Text('Extract', color=BCOLOR).move_to(boxext)
        self.play(
            FadeIn(boxext),
            Write(extract),
        )
        arrows = Arrow(msk.get_right(), boxext.get_left())
        arrowi = Arrow(id.get_top(), boxext.get_bottom())
        self.play(
            Create(arrows),
            Create(arrowi),
        )
        sk = Text('sk').next_to(boxext, 8*RIGHT).scale(.8)
        arrows = Arrow(boxext.get_right(), sk.get_left())
        self.play(
            Create(arrows),
            Create(sk),
        )
        self.wait()

        boxdec = Rectangle(height=1.4, width=5, fill_opacity=1).move_to((11,4,0))
        decrypt = Text('Decrypt', color=BCOLOR).move_to(boxdec)
        self.play(
            FadeIn(boxdec),
            Write(decrypt),
        )
        arrowct2 = Arrow(ct.get_right(), boxdec)
        arrowis = Arrow(sk.get_right(), boxdec)
        self.play(
            Create(arrowct2),
            Create(arrowis),
        )
        msg = msg.copy().next_to(boxdec, 7*DOWN)
        msgt = msgt.copy().next_to(msg, DOWN)
        arrowm = Arrow(boxdec.get_bottom(), msg.get_top())
        self.play(
            Create(arrowm),
            Create(msg),
            Write(msgt),
        )
        self.wait()

        self.play(
            self.camera.frame.animate.scale(0.5).move_to(boxext).shift(DOWN),
            boxext.animate.set_fill(RED),
        )
        self.wait()

        self.play(
            self.camera.frame.animate.move_to(boxkg).shift(RIGHT),
            boxext.animate.set_fill(WHITE),
        )
        self.wait()

        self.remove(idt)
        bfmsk = MathTex('m').move_to(msk)
        bfmpk = MathTex(r'mG_2').move_to(mpk).shift(0.1*LEFT)
        self.play(
            Transform(msk, bfmsk),
            Transform(mpk, bfmpk),
        )
        self.wait()

        self.play(
            self.camera.frame.animate.move_to(boxenc).shift(UP),
        )
        self.wait()

        weil = MathTex('k = e(uDoge, mG_2)', color=BCOLOR,
                       tex_to_color_map={'u': WHITE, 'Doge': WHITE, 'mG_2': WHITE}
                       ).move_to(encrypt)
        self.play(
            Transform(encrypt, weil),
        )
        self.wait()

        mG2 = MathTex('mG_2', color=BCOLOR).move_to(weil[4])
        self.play(
            Write(mG2),
        )
        self.wait()
        
        id2 = id.copy()
        self.add(id2)
        self.play(
            id2.animate.move_to(weil[2]),
        )
        u = MathTex('u', color=BCOLOR).move_to(weil[1])
        self.play(
            Write(u),
        )
        self.wait()

        bfct = MathTex(r'&\mathrm{Enc}_k(\mathrm{msg})\\', '&uG_2').move_to(ct).shift(RIGHT)
        bfact = Arrow(boxenc.get_right(), bfct.get_left())
        bfact2 = Arrow(bfct.get_right(), boxdec)
        self.play(
            Transform(ct, bfct),
            Transform(arrowct, bfact),
            Transform(arrowct2, bfact2),
        )
        self.wait()


        self.play(
            self.camera.frame.animate.move_to(boxdec).shift(LEFT),
        )
        self.wait()

        weil2 = MathTex('k = e(mDoge, uG_2)', color=BCOLOR,
                        tex_to_color_map={'m': WHITE, 'Doge': WHITE, 'uG_2': WHITE}
                        ).move_to(decrypt)
        self.play(
            Transform(decrypt, weil2),
        )
        self.wait()

        uG2 = bfct[1].copy()
        self.add(uG2)
        self.play(
            uG2.animate.move_to(weil2[4]).set_fill(BCOLOR),
        )
        self.wait()

        id3 = id.copy().move_to(weil2[2])
        mdec = MathTex('m', color=BCOLOR).move_to(weil2[1])
        self.play(
            FadeIn(id3),
            FadeIn(mdec),
        )
        self.wait()

        self.play(
            self.camera.frame.animate.move_to(boxext).shift(DOWN),
        )
        self.wait()

        id4 = id.copy()
        self.add(id4)
        self.play(
            id4.animate.move_to(boxext),
        )
        mext = MathTex('m').move_to(sk)
        arrowis2 = Arrow(id4.copy().move_to(sk).shift(RIGHT).get_right(), boxdec)
        self.play(
            id4.animate.move_to(sk).shift(RIGHT),
            FadeOut(sk),
            FadeIn(mext),
            Transform(arrowis, arrowis2),
        )
        self.wait()
        
        self.play(
            self.camera.frame.animate.scale(2).move_to(ORIGIN)
        )
        self.wait()

        phi = Text('φ', weight='BOLD', color='#ff6666').move_to(msk).scale(1.2)
        self.play(
            FadeOut(msk),
            FadeIn(phi),
            Circumscribe(phi),
        )
        self.wait()

        phiG2 = Text('φG₂', weight='BOLD', color='#ff6666').move_to(mpk).scale(1.2)
        clock1 = ImageMobject('clock.png').scale(.1).move_to(phiG2).shift(2*LEFT + UP)
        self.play(
            Transform(mpk, phiG2),
            Circumscribe(phiG2),
            FadeIn(clock1),
        )
        self.wait()

        phisk = phi.copy().move_to(mext)
        clock2 = clock1.copy().move_to(phisk).shift(2*LEFT)
        self.play(
            Transform(mext, phisk),
            Circumscribe(phisk),
            FadeIn(clock2),
        )
        self.wait()

        phiG22 = phiG2.copy().set_fill(color='#ff0000').move_to(mG2)
        self.play(
            Transform(mG2, phiG22),
            Circumscribe(phiG22, color=ORANGE),
        )
        self.wait()

        phisk2 = phisk.copy().set_fill(color='#ff0000').move_to(mdec)
        self.play(
            Transform(mdec, phisk2),
            Circumscribe(phisk2, color=ORANGE),
        )
        self.wait()
        
        incog = ImageMobject('doge-glasses.png').scale(.2).move_to(id)
        incog2 = incog.copy().move_to(id2)
        incog3 = incog.copy().move_to(id3)
        incog4 = incog.copy().move_to(id4)
        self.play(
            Transform(id, incog),
            Transform(id2, incog2),
            Transform(id3, incog3),
            Transform(id4, incog4),
        )
        self.wait()
