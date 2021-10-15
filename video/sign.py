from manim import *

BCOLOR = '#416fa9'
config.transparent = True
config.frame_width = 30

Mobject.set_default(
    color='#bbb',
)
Rectangle.set_default(
    color='#bbb',
)
Text.set_default(
    font='Linux Libertine Display',
    weight='BOLD',   
    color='#bbb',
)
        
class Sign(Scene):
    def construct(self):
        ibe = Group()
        boxkg = Rectangle(height=1, width=3, fill_opacity=1).move_to((-10,4,0))
        keygen = Text('KeyGen', color=BCOLOR).move_to(boxkg)
        ibe.add(boxkg, keygen)
        msk = Text('msk').next_to(boxkg, 3*UP + 7*RIGHT).scale(.8)
        mpk = Text('pk').next_to(boxkg, 3*DOWN + 7*RIGHT).scale(.8)
        arrows = Arrow(boxkg, msk)
        arrowp = Arrow(boxkg, mpk)
        ibe.add(arrows, arrowp, msk, mpk)

        boxenc = Rectangle(height=1.4, width=5, fill_opacity=1).move_to((0,1,0))
        encrypt = Text('Encrypt', color=BCOLOR).move_to(boxenc)
        ibe.add(boxenc, encrypt)
        id = ImageMobject('doge.png').scale(.2).next_to(boxenc, 7*UP)
        ibe.add(id)
        msg = VGroup(
            Rectangle(height=0.5, width=1),
            Line((-0.5, 0.2, 0), ORIGIN),
            Line((0.5, 0.2, 0), ORIGIN),
        ).next_to(boxenc, 14*LEFT)
        msgt = Text('msg').next_to(msg, DOWN).scale(.8)
        msgg = VGroup(msg, msgt)
        ibe.add(msgg)
        arrowm = Arrow(msg.get_right(), boxenc.get_left())
        arrowp = Arrow(mpk.get_right(), boxenc)
        arrowi = Arrow(id.get_bottom(), boxenc.get_top())
        ibe.add(arrowm, arrowp, arrowi)
        ct = Text('ct').next_to(boxenc, 4*RIGHT).scale(.8)
        arrowct = Arrow(boxenc.get_right(), ct.get_left())
        ibe.add(arrowct, ct)

        boxext = Rectangle(height=1, width=3, fill_opacity=1).move_to((0,7,0))
        extract = Text('Extract', color=BCOLOR).move_to(boxext)
        ibe.add(boxext, extract)
        arrows = Arrow(msk.get_right(), boxext.get_left())
        arrowi = Arrow(id.get_top(), boxext.get_bottom())
        ibe.add(arrows, arrowi)
        sk = Text('sk').next_to(boxext, 8*RIGHT).scale(.8)
        arrows = Arrow(boxext.get_right(), sk.get_left())
        ibe.add(arrows, sk)

        boxdec = Rectangle(height=1.4, width=5, fill_opacity=1).move_to((11,4,0))
        decrypt = Text('Decrypt', color=BCOLOR).move_to(boxdec)
        ibe.add(boxdec, decrypt)
        arrowct2 = Arrow(ct.get_right(), boxdec)
        arrowis = Arrow(sk.get_right(), boxdec)
        ibe.add(arrowct2, arrowis)
        msgg2 = msgg.copy().next_to(boxdec, 7*DOWN)
        arrowm = Arrow(boxdec.get_bottom(), msgg2.get_top())
        ibe.add(arrowm, msgg2)

        self.play(FadeIn(ibe))
        self.wait()

        ######
        
        rnd = Text('rnd').move_to(msg)

        self.play(
            msgg.animate.move_to(id),
            FadeOut(id),
            FadeOut(msgg2),
        )

        sig = Text('sig').move_to(sk)
        sign = Text('Sign', color=BCOLOR).move_to(extract)
        self.play(
            Transform(sk, sig),
            Transform(extract, sign),
            Circumscribe(sig),
            Circumscribe(boxext),
        )
        self.wait()

        self.play(
            Write(rnd),
            Circumscribe(rnd),
        )
        ver1 = Text('Verify.0', color=BCOLOR).move_to(encrypt)
        self.play(
            Transform(encrypt, ver1),
            Circumscribe(boxenc),
        )
        ver2 = Text('Verify.1', color=BCOLOR).move_to(decrypt)
        self.play(
            Transform(decrypt, ver2),
            Circumscribe(boxdec),
        )
        check = Text("rnd' == rnd ?").move_to(msgg2)
        self.play(
            Write(check),
            Circumscribe(check),
        )
        self.wait(10)
