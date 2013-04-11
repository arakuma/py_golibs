# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Test Module
# Purpose:
#
# Author:      Si Wei
#
# Created:     10/04/2013
# Copyright:   (c) Si Wei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from go.go_game import *
from sgf.sgf_parser import *

test_sgf = '''
(;FF[4]GM[1]SZ[19]AP[SGFC:1.16]

EV[21st Meijin]
RO[2 (final)]
PB[Takemiya Masaki]
BR[9 dan]
PW[Cho Chikun]
WR[9 dan]
KM[5.5]
DT[1996-10-18,19]
RE[W+Resign]
TM[28800]
SO[Go World #78]
US[Arno Hollosi]

FG[257:Figure 1]PM[1];B[pd];W[dp];B[pp];W[dd];B[pj];W[nc];B[oe]
;W[qc];B[pc];W[qd]
(;B[qf];W[rf];B[rg];W[re];B[qg];W[pb];B[ob];W[qb]
(;B[mp];W[fq];B[ci];W[cg];B[dl];W[cn];B[qo];W[ec];B[jp];W[jd]
;B[ei];W[eg];B[kk]LB[qq:a][dj:b][ck:c][qp:d]N[Figure 1];W[me]
FG[257:Figure 2];B[kf];W[ke];B[lf];W[jf];B[jg]
(;W[mf];B[if];W[je];B[ig];W[mg];B[mj];W[mq];B[lq];W[nq]
(;B[lr];W[qq];B[pq];W[pr];B[rq];W[rr];B[rp];W[oq];B[mr];W[oo]
;B[mn]
(;W[nr];B[qp]LB[kd:a][kh:b]N[Figure 2];W[pk]FG[257:Figure 3]
;B[pm];W[oj];B[ok];W[qr];B[os];W[ol];B[nk];W[qj];B[pi];W[pl]
;B[qm];W[ns];B[sr];W[om];B[op];W[qi];B[oi]
(;W[rl];B[qh];W[rm];B[rn];W[ri];B[ql];W[qk];B[sm];W[sk];B[sh]
;W[og];B[oh];W[np];B[no];W[mm];B[nn];W[lp];B[kp];W[lo];B[ln]
;W[ko];B[mo];W[jo];B[km]N[Figure 3])
(;VW[ja][jb][jc][jd][je][jf][jg][jh][ji][jj][jk][jl][jm][jn]
[jo][jp][jq][jr][js][ka][kb][kc][kd][ke][kf][kg][kh][ki][kj]
[kk][kl][km][kn][ko][kp][kq][kr][ks][la][lb][lc][ld][le][lf]
[lg][lh][li][lj][lk][ll][lm][ln][lo][lp][lq][lr][ls][ma][mb]
[mc][md][me][mf][mg][mh][mi][mj][mk][ml][mm][mn][mo][mp][mq]
[mr][ms][na][nb][nc][nd][ne][nf][ng][nh][ni][nj][nk][nl][nm]
[nn][no][np][nq][nr][ns][oa][ob][oc][od][oe][of][og][oh][oi]
[oj][ok][ol][om][on][oo][op][oq][or][os][pa][pb][pc][pd][pe]
[pf][pg][ph][pi][pj][pk][pl][pm][pn][po][pp][pq][pr][ps][qa]
[qb][qc][qd][qe][qf][qg][qh][qi][qj][qk][ql][qm][qn][qo][qp]
[qq][qr][qs][ra][rb][rc][rd][re][rf][rg][rh][ri][rj][rk][rl]
[rm][rn][ro][rp][rq][rr][rs][sa][sb][sc][sd][se][sf][sg][sh]
[si][sj][sk][sl][sm][sn][so][sp][sq][sr][ss]W[ql]FG[257:Dia. 6]
MN[1];B[rm];W[ph];B[oh];W[pg];B[og];W[pf];B[qh];W[qe];B[sh]
;W[of];B[sj]TR[oe][pd][pc][ob]LB[pe:a][sg:b][si:c]N[Diagram 6]
))
(;VW[jj][jk][jl][jm][jn][jo][jp][jq][jr][js][kj][kk][kl][km]
[kn][ko][kp][kq][kr][ks][lj][lk][ll][lm][ln][lo][lp][lq][lr]
[ls][mj][mk][ml][mm][mn][mo][mp][mq][mr][ms][nj][nk][nl][nm]
[nn][no][np][nq][nr][ns][oj][ok][ol][om][on][oo][op][oq][or]
[os][pj][pk][pl][pm][pn][po][pp][pq][pr][ps][qj][qk][ql][qm]
[qn][qo][qp][qq][qr][qs][rj][rk][rl][rm][rn][ro][rp][rq][rr]
[rs][sj][sk][sl][sm][sn][so][sp][sq][sr][ss]W[no]FG[257:Dia. 5]
MN[1];B[pn]N[Diagram 5]))
(;B[pr]FG[257:Dia. 4]MN[1];W[kq];B[lp];W[lr];B[jq];W[jr];B[kp]
;W[kr];B[ir];W[hr]LB[is:a][js:b][or:c]N[Diagram 4]))
(;W[if]FG[257:Dia. 3]MN[1];B[mf];W[ig];B[jh]LB[ki:a]N[Diagram 3]
))
(;VW[aa][ab][ac][ad][ae][af][ag][ah][ai][aj][ak][ba][bb][bc]
[bd][be][bf][bg][bh][bi][bj][bk][ca][cb][cc][cd][ce][cf][cg]
[ch][ci][cj][ck][da][db][dc][dd][de][df][dg][dh][di][dj][dk]
[ea][eb][ec][ed][ee][ef][eg][eh][ei][ej][ek][fa][fb][fc][fd]
[fe][ff][fg][fh][fi][fj][fk][ga][gb][gc][gd][ge][gf][gg][gh]
[gi][gj][gk][ha][hb][hc][hd][he][hf][hg][hh][hi][hj][hk][ia]
[ib][ic][id][ie][if][ig][ih][ii][ij][ik][ja][jb][jc][jd][je]
[jf][jg][jh][ji][jj][jk][ka][kb][kc][kd][ke][kf][kg][kh][ki]
[kj][kk][la][lb][lc][ld][le][lf][lg][lh][li][lj][lk][ma][mb]
[mc][md][me][mf][mg][mh][mi][mj][mk][na][nb][nc][nd][ne][nf]
[ng][nh][ni][nj][nk][oa][ob][oc][od][oe][of][og][oh][oi][oj]
[ok][pa][pb][pc][pd][pe][pf][pg][ph][pi][pj][pk][qa][qb][qc]
[qd][qe][qf][qg][qh][qi][qj][qk][ra][rb][rc][rd][re][rf][rg]
[rh][ri][rj][rk][sa][sb][sc][sd][se][sf][sg][sh][si][sj][sk]
W[oc]FG[257:Dia. 2]MN[1];B[md];W[mc];B[ld]N[Diagram 2]))
(;VW[aa][ab][ac][ad][ae][af][ag][ah][ai][aj][ba][bb][bc][bd]
[be][bf][bg][bh][bi][bj][ca][cb][cc][cd][ce][cf][cg][ch][ci]
[cj][da][db][dc][dd][de][df][dg][dh][di][dj][ea][eb][ec][ed]
[ee][ef][eg][eh][ei][ej][fa][fb][fc][fd][fe][ff][fg][fh][fi]
[fj][ga][gb][gc][gd][ge][gf][gg][gh][gi][gj][ha][hb][hc][hd]
[he][hf][hg][hh][hi][hj][ia][ib][ic][id][ie][if][ig][ih][ii]
[ij][ja][jb][jc][jd][je][jf][jg][jh][ji][jj][ka][kb][kc][kd]
[ke][kf][kg][kh][ki][kj][la][lb][lc][ld][le][lf][lg][lh][li]
[lj][ma][mb][mc][md][me][mf][mg][mh][mi][mj][na][nb][nc][nd]
[ne][nf][ng][nh][ni][nj][oa][ob][oc][od][oe][of][og][oh][oi]
[oj][pa][pb][pc][pd][pe][pf][pg][ph][pi][pj][qa][qb][qc][qd]
[qe][qf][qg][qh][qi][qj][ra][rb][rc][rd][re][rf][rg][rh][ri]
[rj][sa][sb][sc][sd][se][sf][sg][sh][si][sj]B[qe]FG[257:Dia. 1]
MN[1];W[re];B[qf];W[rf];B[qg];W[pb];B[ob];W[qb]LB[rg:a]N[Diagram 1]
))
'''

def main():
    sgfParser = SgfParser()
    game = sgfParser.read(test_sgf)
    print game.info.event,game.info.black_player_name,game.info.white_player_name,\
    game.kifuInfo.app_name,game.kifuInfo.app_version

if __name__ == '__main__':
    main()
