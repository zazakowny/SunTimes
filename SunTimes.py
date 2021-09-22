import math
import datetime, pytz

def SunPosition(lat,lon,d,m,y,req,tz):
    tshift=pytz.timezone(tz).localize(datetime.datetime(y,m,d)).strftime('%z')
    tshift=int((int(tshift)/100))
    J = 367*y-int(7*(y+int((m+9)/12))/4)+int(275*m/9)+d-730531.5
    Cent = J/36525
    L = (4.8949504201433+628.331969753199*Cent)%6.28318530718
    G = (6.2400408+628.3019501*Cent)%6.28318530718
    O = 0.409093-0.0002269*Cent
    F = 0.033423*math.sin(G)+0.00034907*math.sin(2*G);
    E = 0.0430398*math.sin(2*(L+F)) - 0.00092502*math.sin(4*(L+F)) - F
    A = math.asin(math.sin(O)*math.sin(L+F))
    C = (math.sin(0.017453293*req)-math.sin(0.017453293*lat)*math.sin(A)) /(math.cos(0.017453293*lat)*math.cos(A))
    Wsch = (math.pi - (E+0.017453293*lon+1*math.acos(C)))*57.29577951/15+tshift
    Tran = (math.pi - (E+0.017453293*lon))*57.29577951/15+tshift
    Zach = (math.pi - (E+0.017453293*lon+(-1)*math.acos(C)))*57.29577951/15+tshift
    Day=Zach-Wsch
    Wsch = '{0:02.0f}:{1:02.0f}'.format(*divmod(Wsch * 60, 60))
    Tran = '{0:02.0f}:{1:02.0f}'.format(*divmod(Tran * 60, 60))
    Zach = '{0:02.0f}:{1:02.0f}'.format(*divmod(Zach * 60, 60))
    Day =  '{0:02.0f}:{1:02.0f}'.format(*divmod(Day * 60, 60))
    print("Day length\tSunrise\t\tTransit\tSunset")
    print(Day,"\t\t",Wsch,"\t\t",Tran,"\t\t",Zach,"\nAs of %d-%d-%d (%s - UTC+%d)"%(y,m,d,tz,tshift))
    return (Wsch,Tran,Zach)

# Req = -0.833 - For sunrise and sunset
# Req = -6 - civil twilight
# Req = -12 - nautical twilight
# Req = -18 - astronomical twilight 


now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year
lat = 49.9527772
lon = 19.9718352
req = -0.833
tz='Europe/Warsaw'

w,t,z=SunPosition(lat,lon,day,month,year,req,tz)
