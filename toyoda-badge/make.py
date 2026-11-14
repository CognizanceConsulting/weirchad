import cv2, numpy as np, trimesh, sys
from shapely.geometry import Polygon
from shapely.ops import unary_union
from shapely import affinity
img=cv2.imread(sys.argv[1]); out=sys.argv[2]
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask=((hsv[:,:,1]>60)&(hsv[:,:,2]<230)).astype(np.uint8)*255
mask[:15,:]=0  # drop stray text at very top
mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
cv2.imwrite(out+'/mask.png',mask)
cs,h=cv2.findContours(mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
h=h[0]; polys=[]
for i,c in enumerate(cs):
    if h[i][3]!=-1 or cv2.contourArea(c)<200: continue
    holes=[]; j=h[i][2]
    while j!=-1:
        if cv2.contourArea(cs[j])>50: holes.append(cs[j][:,0,:])
        j=h[j][0]
    p=Polygon(c[:,0,:],[x for x in holes]).buffer(0)
    polys.append(p.simplify(0.6))
g=unary_union(polys)
g=affinity.scale(g,1,-1,origin=(0,0))
minx,miny,maxx,maxy=g.bounds
W=float(sys.argv[3]) if len(sys.argv)>3 else 150.0
s=W/(maxx-minx)
g=affinity.translate(g,-minx,-miny); g=affinity.scale(g,s,s,origin=(0,0))
g=g.buffer(0.15,join_style=1).buffer(-0.15,join_style=1)  # smooth jaggies
print('size mm: %.1f x %.1f'%(g.bounds[2]-g.bounds[0],g.bounds[3]-g.bounds[1]))
def ext(geom,hgt,z=0):
    geoms=getattr(geom,'geoms',[geom]); ms=[]
    for p in geoms:
        m=trimesh.creation.extrude_polygon(p,hgt); m.apply_translation([0,0,z]); ms.append(m)
    return trimesh.util.concatenate(ms)
# parts: emblem = biggest; letters = rest
parts=sorted(getattr(g,'geoms',[g]),key=lambda p:-p.area)
emblem=parts[0]; letters=unary_union(parts[1:])
# Version A: one-piece badge. 1.6mm backer (silhouette offset 2.5mm, holes kept) + 2.4mm raised design
backer=g.buffer(3.2,join_style=1).buffer(-0.7,join_style=1)
# keep the big see-through holes in the emblem
backer=Polygon(backer.exterior) if backer.geom_type=='Polygon' else unary_union([Polygon(b.exterior) for b in backer.geoms])
holes=[Polygon(r) for r in emblem.interiors]
holes=[hh.buffer(-2.5) for hh in holes if hh.buffer(-2.5).area>20]
from shapely.geometry import box
backer=unary_union([backer,box(0,-2.5,W,2.0)]).difference(unary_union(holes))
A=trimesh.boolean.union([ext(backer,1.6),ext(g,2.4,1.6)],engine='manifold')
A.export(out+'/toyoda_badge_onepiece.stl')
# Version B: cut-out style, 3mm thick, emblem and letters separate
ext(emblem,3.0).export(out+'/toyoda_emblem_only.stl')
ext(letters,3.0).export(out+'/toyoda_letters.stl')
# preview
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(10,6))
for geom,col in [(backer,'#555'),(g,'#111')]:
    for p in getattr(geom,'geoms',[geom]):
        x,y=p.exterior.xy; ax.fill(x,y,color=col)
        for r in p.interiors: x,y=r.xy; ax.fill(x,y,color='white')
ax.set_aspect('equal'); ax.set_title('One-piece badge preview (dark = raised 4.0 mm, grey = 1.6 mm backer)')
plt.savefig(out+'/preview.png',dpi=110,bbox_inches='tight')
print('watertight',A.is_watertight, A.bounds)
