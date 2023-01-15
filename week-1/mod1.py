def batting(x):
    name=x.get("name")
    runs=x.get("runs")
    four=x.get("4")
    six=x.get("6")
    balls=x.get("balls")
    
    pts=runs/2
    if runs>=50:
        pts+=5
    if runs>=100:
        pts+=10

    sr=(runs*100)/balls
    if sr>=80 and sr<=100:
        pts+=2
    if sr>100:
        pts+=4
    
    pts+=four
    pts+=2*six

    return {"name":name,"batscore":pts}

def bowling(x):
    name=x.get("name")
    runs=x.get("runs")
    wkts=x.get("wkts")
    overs=x.get("overs")
    field=x.get("field")

    pts=10*wkts
    if wkts>=3:
        pts+=5
    if wkts>=5:
        pts+=10

    er=runs/overs
    if er>=3.5 and er<=4.5:
        pts+=4
    if er>=2 and er<3.5:
        pts+=7
    if er<2:
        pts+=10
    

    return {"name":name,"ballscore":pts}





