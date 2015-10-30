import numpy as n, pylab as p


H=n.hstack

N=200000
n1=H((n.random.normal(0,1,100000),n.random.normal(0,1,100000)))
n2=H((n.random.normal(3,3,100000),n.random.normal(-.4,.17,100000)))

bins=n.linspace(-12,16.,100)
values1,base1=n.histogram(n1,bins=bins)
values2,base2=n.histogram(n2,bins=bins)

n1_=values1
n2_=values2

n1__=n.cumsum(n1_)
n2__=n.cumsum(n2_)


#p.plot(base1[:-1], n1__/20000, c='blue',linewidth=3)
#p.plot(base2[:-1], n2__/20000, c='red' ,linewidth=3)
#p.plot(base1[:-1], n1__/200000, "--",c="k", linewidth=5,alpha=.7,label=r"$F_n$")
p.plot(base1[:-1], n1__/200000, "k-.^", linewidth=5,alpha=.7,label=r"$F_n$")
#p.plot(base1[:-1], n1__/200000, c="k", linewidth=2,alpha=.7,label=r"$F_n$")
p.plot(base2[:-1], n2__/200000, "k-o",linewidth=5 ,alpha=.7,label=r"$F_{n'}$")
#p.plot(base2[:-1], n2__/200000, c="k",linewidth=2 ,alpha=.7,label=r"$F_{n'}$")
p.legend(loc="lower right")
p.ylim(-.05,1.05)
p.xlim(-12.6,16.5)

dd=n.abs(n1__-n2__)
maxi=n.argsort(dd)[-1]
mx=base1[maxi]
my1=n1__[maxi]/N
my2=n2__[maxi]/N
mx_=mx-7
p.plot((mx_,mx_),(my1,my2),"k",linewidth=3)
p.plot((mx_-1,mx_+1),(my1,my1),"k",linewidth=3)
p.plot((mx_-1,mx_+1),(my2,my2),"k",linewidth=3)

p.text(mx-12,(my1+my2)/2,r"$D_{n,n'}$",fontsize=25)


p.plot((mx_+1.5,mx),(my1,my1),"k-.",linewidth=1)
p.plot((mx_+1.5,mx),(my2,my2),"k-.",linewidth=1)
p.ylabel("F",fontsize=15)
p.xlabel("X",fontsize=15)

p.show()
