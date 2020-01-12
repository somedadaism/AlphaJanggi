
GAME_ROWS = 10
GAME_COLS = 9
PLAYER_CHO = 0
PLAYER_HAN = 1

KING=1; CHA=2; PO=3; MA=4; SANG=5; SA=6; ZOL=7
maap=[[0,-1,-1,-2], [0,-1,1,-2], [1,0,2,-1], [1,0,2,1], [0,1,1,2], [0,1,-1,2], [-1,0,-2,-1], [-1,0,-2,1]]
sangap=[[0,-1,-1,-2,-2,-3], [0,-1,1,-2,2,-3], [1,0,2,-1,3,-2], [1,0,2,1,3,2],
    [0,1,1,2,2,3], [0,1,-1,2,-2,3], [-1,0,-2,1,-3,2], [-1,0,-2,-1,-3,-2]]
INITIAL_STATE = ((2,0,0,6,0,6,0,0,2),(0,0,0,0,1,0,0,0,0),(0,3,0,0,0,0,0,3,0),(7,0,7,0,7,0,7,0,7),
    (0,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0),(17,0,17,0,17,0,17,0,17),(0,13,0,0,0,0,0,13,0),
    (0,0,0,0,11,0,0,0,0),(12,0,0,16,0,16,0,0,12))
MAX_TURN = 202

def encode_lists(pan, step):
    s = ""
    for y in range(10):
        for x in range(9):
            s += str(chr(pan[y][x]+ord('a')))
    return s + str(step)

def decode_binary(state_str):
    pan = []
    for y in range(10):
        pan.append([])
        for x in range(9):
            pan[y].append(ord(state_str[y*9+x])-ord('a'))
    return pan

def possible_moves(pan_str, player, step):
    pan = decode_binary(pan_str)
    moven = []
    if step<2:
        for i in range(4): moven.append(10000+i)
    else:
        for y in range(10):
            for x in range(9):
                ki=pan[y][x]; alk=ki//10
                if ki>0 and alk == player:
                    k=y//7*7
                    if ki%10== KING or ki%10== SA:
                        if(x==4 and (y==1 or y==8)):
                            for i in range(-1,2):
                                for j in range(3,6):
                                    a=pan[i+y][j]
                                    if a==0 or a//10 != alk: moven.append((y*9+x)*100+(i+y)*9+j)
                        else:
                            for i in range(3):
                                for j in range(3,6):
                                    if(abs(i+k-y)+abs(j-x)<2 or (i==1 and j==4)):
                                        a=pan[i+k][j]
                                        if(a==0 or a//10!=alk):	moven.append((y*9+x)*100+(i+k)*9+j)
                    elif ki%10 == CHA:
                        if(x==4 and (y==1 or y==8)):
                            for i in range(-1,2,2):
                                for j in range(3,6,2):
                                    a=pan[i+y][j]
                                    if(a==0 or a//10!=alk): moven.append((y*9+x)*100+(i+y)*9+j)
                        elif((x==3 or x==5) and (y==k or y==k+2)):
                            a=pan[k+1][4]
                            if(a==0 or a//10!=alk): moven.append((y*9+x)*100+(k+1)*9+4)
                            b=2*k+2-y; a=pan[b][8-x]
                            if(pan[k+1][4]==0 and (a==0 or a//10!=alk)): moven.append((y*9+x)*100+b*9+8-x)
                        for i in range(x+1,9):
                            a=pan[y][i]
                            if(a==0 or a//10!=alk): moven.append((y*9+x)*100+y*9+i)
                            if(a>0): break
                        for i in range(x-1,-1,-1):
                            a=pan[y][i]
                            if(a==0 or a//10!=alk): moven.append((y*9+x)*100+y*9+i)
                            if(a>0): break
                        for i in range(y+1,10):
                            a=pan[i][x]
                            if(a==0 or a//10!=alk): moven.append((y*9+x)*100+i*9+x)
                            if(a>0): break
                        for i in range(y-1,-1,-1):
                            a=pan[i][x]
                            if(a==0 or a//10!=alk): moven.append((y*9+x)*100+i*9+x)
                            if(a>0): break
                    elif ki%10 == PO:
                        for i in range(x+1,8):
                            if(pan[y][i]>0):
                                if(pan[y][i]%10!=PO):
                                    for j in range(i+1,9):
                                        a=pan[y][j]
                                        if(a==0 or (a//10!=alk and a%10!=PO)): moven.append((y*9+x)*100+y*9+j)
                                        if(a>0): break
                                break
                        for i in range(x-1,0,-1):
                            if(pan[y][i]>0):
                                if(pan[y][i]%10!=PO):
                                    for j in range(i-1,-1,-1):
                                        a=pan[y][j]
                                        if(a==0 or (a//10!=alk and a%10!=PO)): moven.append((y*9+x)*100+y*9+j)
                                        if(a>0): break
                                break
                        for i in range(y+1,9):
                            if(pan[i][x]>0):
                                if(pan[i][x]%10!=PO):
                                    for j in range(i+1,10):
                                        a=pan[j][x]
                                        if(a==0 or (a//10!=alk and a%10!=PO)): moven.append((y*9+x)*100+j*9+x)
                                        if(a>0): break
                                break
                        for i in range(y-1,0,-1):
                            if(pan[i][x]>0):
                                if(pan[i][x]%10!=PO):
                                    for j in range(i-1,-1,-1):
                                        a=pan[j][x]
                                        if(a==0 or (a//10!=alk and a%10!=PO)): moven.append((y*9+x)*100+j*9+x)
                                        if(a>0): break
                                break
                        if((x==3 or x==5) and (y==k or y==k+2)):
                            a=pan[k+1][4]; c=2*k+2-y; b=pan[c][8-x]
                            if(a>0 and a%10!=PO and (b==0 or (b//10!=alk and b%10!=PO))):
                                moven.append((y*9+x)*100+c*9+8-x)
                    elif ki%10 == MA:
                        for i in range(8):
                            x1=x+maap[i][2]; y1=y+maap[i][3]
                            if(y1>=0 and y1<10 and x1>=0 and x1<9):
                                a=pan[y1][x1]
                                if((a==0 or a//10!=alk) and pan[y+maap[i][1]][x+maap[i][0]]==0):
                                    moven.append((y*9+x)*100+y1*9+x1)
                    elif ki%10 == SANG:
                        for i in range(8):
                            x1=x+sangap[i][4]; y1=y+sangap[i][5]
                            if(y1>=0 and y1<10 and x1>=0 and x1<9):
                                a=pan[y1][x1]
                                if((a==0 or a//10!=alk) and pan[y+sangap[i][1]][x+sangap[i][0]]==0 and pan[y+sangap[i][3]][x+sangap[i][2]]==0):
                                    moven.append((y*9+x)*100+y1*9+x1)
                    elif ki%10 == ZOL:
                        ad=-1 if alk==1 else 1
                        for i in range(-1,2,):
                            x1=x+i; y1=y+(ad if i==0 else 0)
                            if(x1>=0 and x1<9 and y1>=0 and y1<10):
                                a=pan[y1][x1]
                                if(a==0 or a//10!=alk): moven.append((y*9+x)*100+y1*9+x1)
                        if(x==4 and y==k+1):
                            for i in range(-1,2,2):
                                b=y+ad; a=pan[b][x+i]
                                if(a==0 or a//10!=alk):	moven.append((y*9+x)*100+b*9+x+i)
                        if((x==3 or x==5) and (y==2 or y==7)):
                            a=pan[k+1][4]
                            if(a==0 or a//10!=alk): moven.append((y*9+x)*100+(k+1)*9+4)
        moven.append(0)
    return moven

gungd = (
  0, 0, 0, 1, 0, 1, 0, 0, 0,
  0, 0, 0, 0, 1, 0, 0, 0, 0,
  0, 0, 0, 1, 0, 1, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 1, 0, 1, 0, 0, 0,
  0, 0, 0, 0, 1, 0, 0, 0, 0,
  0, 0, 0, 1, 0, 1, 0, 0, 0)
sangv=(
   0,  0,-19,  0,  0,  0,-17,  0,  0,
   0,-11,  0,  0,  0,  0,  0, -7,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  0,  0,  0,  0,  0,  0,  0,  0,
   0,  7,  0,  0,  0,  0,  0, 11,  0,
   0,  0, 17,  0,  0,  0, 19,  0,  0)

def kingSafe(pan, player, arr):
    oplayer = (1-player)*10
    pcs = []
    for d in range(10):
        for j in range(9):
            k=pan[d][j]
            if(k==10-oplayer+KING): kingp=d*9+j; kingx = j; kingy = d
            elif(k>KING+oplayer and k<9+oplayer and k!=SA+oplayer): pcs.append([d*9+j, k%10])
    kings = []; kings.append(kingp)
    for d in range(-1,2):
        x=kingx+d
        if x>2 and x<6: kings.append(kingy*9+x)
    for d in range(-1,2):
        y=kingy+d
        if y>=0 and y<10 and (y<3 or y>6): kings.append(y*9+kingx)
    if gungd[kingp]:
        for d in range(-1, 3, 2):
            for j in range(-1,3, 2):
                x=kingx+j; y=kingy+d
                if x>2 and x<6 and ((kingy<3 and y>=0 and y<3) or (kingy>2 and y>6 and y<10)):
                    kings.append(y*9+x)
    for kingp in kings:
        kingx = kingp%9; kingy = kingp//9
        for piece in pcs:
            p=piece[0]; x=p%9; y=p//9
            if piece[1] == CHA:
                if(x==kingx):
                    d=1 if y<kingy else -1; y+=d
                    while(y!=kingy and pan[y][x]==0): y+=d
                    if(y==kingy): arr[y][x]=1
                elif(y==kingy):
                    d=1 if x<kingx else -1; x+=d
                    while(x!=kingx and pan[y][x]==0): x+=d
                    if(x==kingx): arr[y][x]=1
                elif(gungd[p] and gungd[kingp] and abs(y-kingy)<4):
                    d=abs(x-kingx)
                    if(d==1 or (d==2 and pan[1 if y<4 else 8][4]==0)): arr[y][x]=1
            elif piece[1] == PO:
                if(x==kingx):
                    d=1 if y<kingy else -1; y+=d
                    while(y!=kingy and pan[y][x]==0): y+=d
                    if(y!=kingy and pan[y][x]%10!=PO):
                        y+=d
                        while(y!=kingy and pan[y][x]==0): y+=d
                        if(y==kingy): arr[y][x]=1
                elif(y==kingy):
                    d=1 if x<kingx else -1; x+=d
                    while(x!=kingx and pan[y][x]==0): x+=d
                    if(x!=kingx and pan[y][x]%10!=PO):
                        x+=d
                        while(x!=kingx and pan[y][x]==0): x+=d
                        if(x==kingx): arr[y][x]=1
                elif(gungd[p] and gungd[kingp] and abs(y-kingy)==2):
                    k=pan[1 if y<4 else 8][4]
                    if(k%10!=PO and k>0): arr[y][x]=1
            elif piece[1] == MA:
                d=abs(x-kingx); k=abs(y-kingy)
                if(d+k==3 and d>0 and d<3):
                    if(d==1): y+=-1 if kingy<y else 1
                    else: x+=-1 if kingx<x else 1
                    if(pan[y][x]==0): arr[y][x]=1
            elif piece[1] == SANG:
                d=abs(x-kingx); k=abs(y-kingy)
                if(d+k==5 and d>1 and d<4):
                    if(d==2): y+=-1 if kingy<y else 1
                    else: x+=-1 if kingx<x else 1
                    if(pan[y][x]==0):
                        k=sangv[kingp-p+31]+p
                        if(pan[k//9][k%9]==0): arr[y][x]=1
            elif piece[1] == ZOL:
                if(y==kingy):
                    if(abs(x-kingx)==1): arr[y][x]=1
                elif(kingy==y+(-1 if oplayer>0 else 1) and (x==kingx or (gungd[p] and gungd[kingp]))):
                    arr[y][x]=1
    return arr

def move(pan_str, move, step):
    pan = decode_binary(pan_str)
    if(move>=10000):
        if step<1:
            if move==10000:
                pan[9][1]=14; pan[9][2]=15; pan[9][6]=14; pan[9][7]=15
            elif move==10001:
                pan[9][1]=15; pan[9][2]=14; pan[9][6]=15; pan[9][7]=14
            elif move==10002:
                pan[9][1]=14; pan[9][2]=15; pan[9][6]=15; pan[9][7]=14
            else:
                pan[9][1]=15; pan[9][2]=14; pan[9][6]=14; pan[9][7]=15
        else:
            if move==10000:
                pan[0][1]=5; pan[0][2]=4; pan[0][6]=5; pan[0][7]=4
            elif move==10001:
                pan[0][1]=4; pan[0][2]=5; pan[0][6]=4; pan[0][7]=5
            elif move==10002:
                pan[0][1]=4; pan[0][2]=5; pan[0][6]=5; pan[0][7]=4
            else:
                pan[0][1]=5; pan[0][2]=4; pan[0][6]=4; pan[0][7]=5
        return encode_lists(pan, step+1), False
    elif move == 0:
        return encode_lists(pan, step+1), False
    else:
        spos = move // 100; tpos = move % 100; y0=spos//9; x0=spos%9; y1=tpos//9; x1=tpos%9
        captured = pan[y1][x1]
        piece = pan[y0][x0]
        pan[y1][x1] = piece
        pan[y0][x0] = 0

        return encode_lists(pan, step+1), True if captured%10 == KING else False
