#!/usr/bin/env python

from __future__ import division

import colorsys
import copy

from collections import defaultdict


all_pos = {'L1': None,
'K1': None,
'J1': None,
'H1': None,
'G1': None,
'F1': None,
'E1': None,
'N2': None,
'M2': None,
'L2': None,
'K2': None,
'J2': None,
'H2': None,
'G2': None,
'F2': None,
'E2': None,
'D2': None,
'C2': None,
'P3': None,
'N3': None,
'M3': None,
'L3': None,
'K3': None,
'J3': None,
'H3': None,
'G3': None,
'F3': None,
'E3': None,
'D3': None,
'C3': None,
'B3': None,
'P4': None,
'N4': None,
'M4': None,
'L4': None,
'K4': None,
'J4': None,
'H4': None,
'G4': None,
'F4': None,
'E4': None,
'D4': None,
'C4': None,
'B4': None,
'R5': None,
'P5': None,
'N5': None,
'M5': None,
'L5': None,
'K5': None,
'J5': None,
'H5': None,
'G5': None,
'F5': None,
'E5': None,
'D5': None,
'C5': None,
'B5': None,
'A5': None,
'R6': None,
'P6': None,
'N6': None,
'M6': None,
'L6': None,
'K6': None,
'J6': None,
'H6': None,
'G6': None,
'F6': None,
'E6': None,
'D6': None,
'C6': None,
'B6': None,
'A6': None,
'R7': None,
'P7': None,
'N7': None,
'M7': None,
'L7': None,
'K7': None,
'J7': None,
'H7': None,
'G7': None,
'F7': None,
'E7': None,
'D7': None,
'C7': None,
'B7': None,
'A7': None,
'R8': None,
'P8': None,
'N8': None,
'M8': None,
'L8': None,
'K8': None,
'J8': None,
'H8': None,
'G8': None,
'F8': None,
'E8': None,
'D8': None,
'C8': None,
'B8': None,
'A8': None,
'R9': None,
'P9': None,
'N9': None,
'M9': None,
'L9': None,
'K9': None,
'J9': None,
'H9': None,
'G9': None,
'F9': None,
'E9': None,
'D9': None,
'C9': None,
'B9': None,
'A9': None,
'R10': None,
'P10': None,
'N10': None,
'M10': None,
'L10': None,
'K10': None,
'J10': None,
'H10': None,
'G10': None,
'F10': None,
'E10': None,
'D10': None,
'C10': None,
'B10': None,
'A10': None,
'R11': None,
'P11': None,
'N11': None,
'M11': None,
'L11': None,
'K11': None,
'J11': None,
'H11': None,
'G11': None,
'F11': None,
'E11': None,
'D11': None,
'C11': None,
'B11': None,
'A11': None,
'P12': None,
'N12': None,
'M12': None,
'L12': None,
'K12': None,
'J12': None,
'H12': None,
'G12': None,
'F12': None,
'E12': None,
'D12': None,
'C12': None,
'B12': None,
'P13': None,
'N13': None,
'M13': None,
'L13': None,
'K13': None,
'J13': None,
'H13': None,
'G13': None,
'F13': None,
'E13': None,
'D13': None,
'C13': None,
'B13': None,
'N14': None,
'M14': None,
'L14': None,
'K14': None,
'J14': None,
'H14': None,
'G14': None,
'F14': None,
'E14': None,
'D14': None,
'C14': None,
'L15': None,
'K15': None,
'J15': None,
'H15': None,
'G15': None,
'F15': None,
'E15': None,
}

numnames = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
}

color_t = r"""\definecolor{{{colorname}}}{{rgb}}{{{r},{g},{b}}}
"""

main_fig_t = r"""
\begin{{figure}}[htbp]
    \centering

    % these dimensions are determined in arrow_dimms.ods

    \def\scale{{{scale}}}

    \def\latWidth{{0.2673473684*\scale}}

    \def\RPVOR{{3*\scale}}
    \def\rectW{{0.75*\scale}}
    \def\RPVIR{{2.7315789474*\scale}}
    \def\BarrelIR{{2.3368421053*\scale}}
    \def\BarrelOR{{2.4078947368*\scale}}
    \def\ShieldIR{{2.4223787816*\scale}}
    \def\ShieldOR{{2.5067965189*\scale}}
    \def\LinerIR{{2.7246166598*\scale}}

    \def\bafCIRx{{0.9357157895*\scale}}
    \def\bafCIRy{{2.0051052632*\scale}}
    \def\bafCORx{{0.9633473684*\scale}}
    \def\bafCORy{{2.0327368421*\scale}}
    \def\bafMIRx{{1.7377578947*\scale}}
    \def\bafMIRy{{1.4704105263*\scale}}
    \def\bafMORx{{1.7653894737*\scale}}
    \def\bafMORy{{1.4980421053*\scale}}

    \tikzset{{Assembly/.style={{
        inner sep=0pt,
        text width=\latWidth in,
        minimum size=\latWidth in,
        draw=black,
        align=center
        }}
    }}

    \def\tkzRPV{{(0,0) circle (\RPVIR) (0,0) circle (\RPVOR)}}
    \def\tkzLiner{{(0,0) circle (\LinerIR) (0,0) circle (\RPVIR)}}
    \def\tkzBarrel{{(0,0) circle (\BarrelIR) (0,0) circle (\BarrelOR)}}
    \def\tkzShields{{(0,0) circle (\ShieldIR) (0,0) circle (\ShieldOR)}}

    \def\tkzBaffCOR{{(-\bafCORx, -\bafCORy) rectangle (\bafCORx, \bafCORy)}}
    \def\tkzBaffCIR{{(-\bafCIRx, -\bafCIRy) rectangle (\bafCIRx, \bafCIRy)}}
    \def\tkzBaffMOR{{(-\bafMORx, -\bafMORy) rectangle (\bafMORx, \bafMORy)}}
    \def\tkzBaffMIR{{(-\bafMIRx, -\bafMIRy) rectangle (\bafMIRx, \bafMIRy) }}
    \def\tkzBaffleC{{ \tkzBaffCIR \tkzBaffCOR }}
    \def\tkzBaffleM{{ \tkzBaffMIR \tkzBaffMOR }}

    \def\tkzBaffCClip{{\tkzBaffCIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}
    \def\tkzBaffMClip{{\tkzBaffMIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}

    \def\highenr{{blue!50}}
    \def\midenr{{yellow!50}}
    \def\lowenr{{red!50}}

    \scalebox{{{scalebox}}}{{

      \begin{{tikzpicture}}[x=1in,y=1in]

        % draw RPV, barrel, liner and shield panels

        {struct}\path[fill=black!90!white,even odd rule] \tkzRPV;
        {struct}\path[fill=black,even odd rule] \tkzLiner;
        {struct}\path[fill=black,even odd rule] \tkzBarrel;
        {struct}\begin{{scope}}
        {struct}  \clip (0,0) -- +(61:\RPVOR) arc (61:29:\RPVOR) --
        {struct}        (0,0) -- +(151:\RPVOR) arc (151:119:\RPVOR) --
        {struct}        (0,0) -- +(241:\RPVOR) arc (241:209:\RPVOR) --
        {struct}        (0,0) -- +(331:\RPVOR) arc (331:299:\RPVOR) -- cycle;
        {struct}  \path[fill=black,even odd rule] \tkzShields;
        {struct}\end{{scope}}

        % draw baffle north/south

        {struct}\begin{{scope}}[even odd rule]
        {struct}  \clip[rotate=90] \tkzBaffMClip;
        {struct}  \path[fill=black] \tkzBaffleC;
        {struct}\end{{scope}}
        {struct}\begin{{scope}}[even odd rule]
        {struct}  \clip \tkzBaffCClip;
        {struct}  \clip \tkzBaffMClip;
        {struct}  \path[fill=black, rotate=90] \tkzBaffleM;
        {struct}\end{{scope}}

        % draw baffle east/west

        {struct}\begin{{scope}}[rotate=90]
        {struct}  \begin{{scope}}[even odd rule]
        {struct}    \clip[rotate=90] \tkzBaffMClip;
        {struct}    \path[fill=black] \tkzBaffleC;
        {struct}  \end{{scope}}
        {struct}  \begin{{scope}}[even odd rule]
        {struct}    \clip \tkzBaffCClip;
        {struct}    \clip \tkzBaffMClip;
        {struct}    \path[fill=black, rotate=90] \tkzBaffleM;
        {struct}  \end{{scope}}
        {struct}\end{{scope}}

        % draw assembly row/column headers

        \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{R}} -- ($(-7*\latWidth,4*\latWidth)$);
        \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{P}} -- ($(-6*\latWidth,6*\latWidth)$);
        \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{N}} -- ($(-5*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{M}} -- ($(-4*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{L}} -- ($(-3*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{K}} -- ($(-2*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{J}} -- ($(-1*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{H}} -- ($(-0*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{G}} -- ($(1*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{F}} -- ($(2*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{E}} -- ($(3*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{D}} -- ($(4*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{C}} -- ($(5*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{B}} -- ($(6*\latWidth,6*\latWidth)$);
        \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{A}} -- ($(7*\latWidth,4*\latWidth)$);

        \begin{{scope}}[rotate=90]
          \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{15}} -- ($(-7*\latWidth,4*\latWidth)$);
          \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{14}} -- ($(-6*\latWidth,6*\latWidth)$);
          \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{13}} -- ($(-5*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{12}} -- ($(-4*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{11}} -- ($(-3*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{10}} -- ($(-2*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{9}} -- ($(-1*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{8}} -- ($(-0*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{7}} -- ($(1*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{6}} -- ($(2*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{5}} -- ($(3*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{4}} -- ($(4*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{3}} -- ($(5*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{2}} -- ($(6*\latWidth,6*\latWidth)$);
          \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{1}} -- ($(7*\latWidth,4*\latWidth)$);
        \end{{scope}}

        % draw fuel assembly nodes

        \node [Assembly, fill=\highenr{coredata[L1_hyper]}] at ($(-3*\latWidth,7*\latWidth)$) {{{coredata[L1_content]}}}; % L1
        \node [Assembly, fill=\highenr{coredata[K1_hyper]}] at ($(-2*\latWidth,7*\latWidth)$) {{{coredata[K1_content]}}}; % K1
        \node [Assembly, fill=\highenr{coredata[J1_hyper]}] at ($(-1*\latWidth,7*\latWidth)$) {{{coredata[J1_content]}}}; % J1
        \node [Assembly, fill=\highenr{coredata[H1_hyper]}] at ($(-0*\latWidth,7*\latWidth)$) {{{coredata[H1_content]}}}; % H1
        \node [Assembly, fill=\highenr{coredata[G1_hyper]}] at ($( 1*\latWidth,7*\latWidth)$) {{{coredata[G1_content]}}}; % G1
        \node [Assembly, fill=\highenr{coredata[F1_hyper]}] at ($( 2*\latWidth,7*\latWidth)$) {{{coredata[F1_content]}}}; % F1
        \node [Assembly, fill=\highenr{coredata[E1_hyper]}] at ($( 3*\latWidth,7*\latWidth)$) {{{coredata[E1_content]}}}; % E1

        \node [Assembly, fill=\highenr{coredata[N2_hyper]}] at ($(-5*\latWidth,6*\latWidth)$) {{{coredata[N2_content]}}}; % N2
        \node [Assembly, fill=\highenr{coredata[M2_hyper]}] at ($(-4*\latWidth,6*\latWidth)$) {{{coredata[M2_content]}}}; % M2
        \node [Assembly, fill=\highenr{coredata[L2_hyper]}] at ($(-3*\latWidth,6*\latWidth)$) {{{coredata[L2_content]}}}; % L2
        \node [Assembly, fill=\lowenr{coredata[K2_hyper]}] at ($(-2*\latWidth,6*\latWidth)$) {{{coredata[K2_content]}}}; % K2
        \node [Assembly, fill=\highenr{coredata[J2_hyper]}] at ($(-1*\latWidth,6*\latWidth)$) {{{coredata[J2_content]}}}; % J2
        \node [Assembly, fill=\lowenr{coredata[H2_hyper]}] at ($(-0*\latWidth,6*\latWidth)$) {{{coredata[H2_content]}}}; % H2
        \node [Assembly, fill=\highenr{coredata[G2_hyper]}] at ($( 1*\latWidth,6*\latWidth)$) {{{coredata[G2_content]}}}; % G2
        \node [Assembly, fill=\lowenr{coredata[F2_hyper]}] at ($( 2*\latWidth,6*\latWidth)$) {{{coredata[F2_content]}}}; % F2
        \node [Assembly, fill=\highenr{coredata[E2_hyper]}] at ($( 3*\latWidth,6*\latWidth)$) {{{coredata[E2_content]}}}; % E2
        \node [Assembly, fill=\highenr{coredata[D2_hyper]}] at ($( 4*\latWidth,6*\latWidth)$) {{{coredata[D2_content]}}}; % D2
        \node [Assembly, fill=\highenr{coredata[C2_hyper]}] at ($( 5*\latWidth,6*\latWidth)$) {{{coredata[C2_content]}}}; % C2

        \node [Assembly, fill=\highenr{coredata[P3_hyper]}] at ($(-6*\latWidth,5*\latWidth)$) {{{coredata[P3_content]}}}; % P3
        \node [Assembly, fill=\highenr{coredata[N3_hyper]}] at ($(-5*\latWidth,5*\latWidth)$) {{{coredata[N3_content]}}}; % N3
        \node [Assembly, fill=\midenr{coredata[M3_hyper]}] at ($(-4*\latWidth,5*\latWidth)$) {{{coredata[M3_content]}}}; % M3
        \node [Assembly, fill=\lowenr{coredata[L3_hyper]}] at ($(-3*\latWidth,5*\latWidth)$) {{{coredata[L3_content]}}}; % L3
        \node [Assembly, fill=\midenr{coredata[K3_hyper]}] at ($(-2*\latWidth,5*\latWidth)$) {{{coredata[K3_content]}}}; % K3
        \node [Assembly, fill=\lowenr{coredata[J3_hyper]}] at ($(-1*\latWidth,5*\latWidth)$) {{{coredata[J3_content]}}}; % J3
        \node [Assembly, fill=\midenr{coredata[H3_hyper]}] at ($(-0*\latWidth,5*\latWidth)$) {{{coredata[H3_content]}}}; % H3
        \node [Assembly, fill=\lowenr{coredata[G3_hyper]}] at ($( 1*\latWidth,5*\latWidth)$) {{{coredata[G3_content]}}}; % G3
        \node [Assembly, fill=\midenr{coredata[F3_hyper]}] at ($( 2*\latWidth,5*\latWidth)$) {{{coredata[F3_content]}}}; % F3
        \node [Assembly, fill=\lowenr{coredata[E3_hyper]}] at ($( 3*\latWidth,5*\latWidth)$) {{{coredata[E3_content]}}}; % E3
        \node [Assembly, fill=\midenr{coredata[D3_hyper]}] at ($( 4*\latWidth,5*\latWidth)$) {{{coredata[D3_content]}}}; % D3
        \node [Assembly, fill=\highenr{coredata[C3_hyper]}] at ($( 5*\latWidth,5*\latWidth)$) {{{coredata[C3_content]}}}; % C3
        \node [Assembly, fill=\highenr{coredata[B3_hyper]}] at ($( 6*\latWidth,5*\latWidth)$) {{{coredata[B3_content]}}}; % B3

        \node [Assembly, fill=\highenr{coredata[P4_hyper]}] at ($(-6*\latWidth,4*\latWidth)$) {{{coredata[P4_content]}}}; % P4
        \node [Assembly, fill=\midenr{coredata[N4_hyper]}] at ($(-5*\latWidth,4*\latWidth)$) {{{coredata[N4_content]}}}; % N4
        \node [Assembly, fill=\midenr{coredata[M4_hyper]}] at ($(-4*\latWidth,4*\latWidth)$) {{{coredata[M4_content]}}}; % M4
        \node [Assembly, fill=\midenr{coredata[L4_hyper]}] at ($(-3*\latWidth,4*\latWidth)$) {{{coredata[L4_content]}}}; % L4
        \node [Assembly, fill=\lowenr{coredata[K4_hyper]}] at ($(-2*\latWidth,4*\latWidth)$) {{{coredata[K4_content]}}}; % K4
        \node [Assembly, fill=\midenr{coredata[J4_hyper]}] at ($(-1*\latWidth,4*\latWidth)$) {{{coredata[J4_content]}}}; % J4
        \node [Assembly, fill=\lowenr{coredata[H4_hyper]}] at ($(-0*\latWidth,4*\latWidth)$) {{{coredata[H4_content]}}}; % H4
        \node [Assembly, fill=\midenr{coredata[G4_hyper]}] at ($( 1*\latWidth,4*\latWidth)$) {{{coredata[G4_content]}}}; % G4
        \node [Assembly, fill=\lowenr{coredata[F4_hyper]}] at ($( 2*\latWidth,4*\latWidth)$) {{{coredata[F4_content]}}}; % F4
        \node [Assembly, fill=\midenr{coredata[E4_hyper]}] at ($( 3*\latWidth,4*\latWidth)$) {{{coredata[E4_content]}}}; % E4
        \node [Assembly, fill=\midenr{coredata[D4_hyper]}] at ($( 4*\latWidth,4*\latWidth)$) {{{coredata[D4_content]}}}; % D4
        \node [Assembly, fill=\midenr{coredata[C4_hyper]}] at ($( 5*\latWidth,4*\latWidth)$) {{{coredata[C4_content]}}}; % C4
        \node [Assembly, fill=\highenr{coredata[B4_hyper]}] at ($( 6*\latWidth,4*\latWidth)$) {{{coredata[B4_content]}}}; % B4

        \node [Assembly, fill=\highenr{coredata[R5_hyper]}] at ($(-7*\latWidth,3*\latWidth)$) {{{coredata[R5_content]}}}; % R5
        \node [Assembly, fill=\highenr{coredata[P5_hyper]}] at ($(-6*\latWidth,3*\latWidth)$) {{{coredata[P5_content]}}}; % P5
        \node [Assembly, fill=\lowenr{coredata[N5_hyper]}] at ($(-5*\latWidth,3*\latWidth)$) {{{coredata[N5_content]}}}; % N5
        \node [Assembly, fill=\midenr{coredata[M5_hyper]}] at ($(-4*\latWidth,3*\latWidth)$) {{{coredata[M5_content]}}}; % M5
        \node [Assembly, fill=\lowenr{coredata[L5_hyper]}] at ($(-3*\latWidth,3*\latWidth)$) {{{coredata[L5_content]}}}; % L5
        \node [Assembly, fill=\midenr{coredata[K5_hyper]}] at ($(-2*\latWidth,3*\latWidth)$) {{{coredata[K5_content]}}}; % K5
        \node [Assembly, fill=\lowenr{coredata[J5_hyper]}] at ($(-1*\latWidth,3*\latWidth)$) {{{coredata[J5_content]}}}; % J5
        \node [Assembly, fill=\midenr{coredata[H5_hyper]}] at ($(-0*\latWidth,3*\latWidth)$) {{{coredata[H5_content]}}}; % H5
        \node [Assembly, fill=\lowenr{coredata[G5_hyper]}] at ($( 1*\latWidth,3*\latWidth)$) {{{coredata[G5_content]}}}; % G5
        \node [Assembly, fill=\midenr{coredata[F5_hyper]}] at ($( 2*\latWidth,3*\latWidth)$) {{{coredata[F5_content]}}}; % F5
        \node [Assembly, fill=\lowenr{coredata[E5_hyper]}] at ($( 3*\latWidth,3*\latWidth)$) {{{coredata[E5_content]}}}; % E5
        \node [Assembly, fill=\midenr{coredata[D5_hyper]}] at ($( 4*\latWidth,3*\latWidth)$) {{{coredata[D5_content]}}}; % D5
        \node [Assembly, fill=\lowenr{coredata[C5_hyper]}] at ($( 5*\latWidth,3*\latWidth)$) {{{coredata[C5_content]}}}; % C5
        \node [Assembly, fill=\highenr{coredata[B5_hyper]}] at ($( 6*\latWidth,3*\latWidth)$) {{{coredata[B5_content]}}}; % B5
        \node [Assembly, fill=\highenr{coredata[A5_hyper]}] at ($( 7*\latWidth,3*\latWidth)$) {{{coredata[A5_content]}}}; % A5

        \node [Assembly, fill=\highenr{coredata[R6_hyper]}] at ($(-7*\latWidth,2*\latWidth)$) {{{coredata[R6_content]}}}; % R6
        \node [Assembly, fill=\lowenr{coredata[P6_hyper]}] at ($(-6*\latWidth,2*\latWidth)$) {{{coredata[P6_content]}}}; % P6
        \node [Assembly, fill=\midenr{coredata[N6_hyper]}] at ($(-5*\latWidth,2*\latWidth)$) {{{coredata[N6_content]}}}; % N6
        \node [Assembly, fill=\lowenr{coredata[M6_hyper]}] at ($(-4*\latWidth,2*\latWidth)$) {{{coredata[M6_content]}}}; % M6
        \node [Assembly, fill=\midenr{coredata[L6_hyper]}] at ($(-3*\latWidth,2*\latWidth)$) {{{coredata[L6_content]}}}; % L6
        \node [Assembly, fill=\lowenr{coredata[K6_hyper]}] at ($(-2*\latWidth,2*\latWidth)$) {{{coredata[K6_content]}}}; % K6
        \node [Assembly, fill=\midenr{coredata[J6_hyper]}] at ($(-1*\latWidth,2*\latWidth)$) {{{coredata[J6_content]}}}; % J6
        \node [Assembly, fill=\lowenr{coredata[H6_hyper]}] at ($(-0*\latWidth,2*\latWidth)$) {{{coredata[H6_content]}}}; % H6
        \node [Assembly, fill=\midenr{coredata[G6_hyper]}] at ($( 1*\latWidth,2*\latWidth)$) {{{coredata[G6_content]}}}; % G6
        \node [Assembly, fill=\lowenr{coredata[F6_hyper]}] at ($( 2*\latWidth,2*\latWidth)$) {{{coredata[F6_content]}}}; % F6
        \node [Assembly, fill=\midenr{coredata[E6_hyper]}] at ($( 3*\latWidth,2*\latWidth)$) {{{coredata[E6_content]}}}; % E6
        \node [Assembly, fill=\lowenr{coredata[D6_hyper]}] at ($( 4*\latWidth,2*\latWidth)$) {{{coredata[D6_content]}}}; % D6
        \node [Assembly, fill=\midenr{coredata[C6_hyper]}] at ($( 5*\latWidth,2*\latWidth)$) {{{coredata[C6_content]}}}; % C6
        \node [Assembly, fill=\lowenr{coredata[B6_hyper]}] at ($( 6*\latWidth,2*\latWidth)$) {{{coredata[B6_content]}}}; % B6
        \node [Assembly, fill=\highenr{coredata[A6_hyper]}] at ($( 7*\latWidth,2*\latWidth)$) {{{coredata[A6_content]}}}; % A6

        \node [Assembly, fill=\highenr{coredata[R7_hyper]}] at ($(-7*\latWidth,1*\latWidth)$) {{{coredata[R7_content]}}}; % R7
        \node [Assembly, fill=\highenr{coredata[P7_hyper]}] at ($(-6*\latWidth,1*\latWidth)$) {{{coredata[P7_content]}}}; % P7
        \node [Assembly, fill=\lowenr{coredata[N7_hyper]}] at ($(-5*\latWidth,1*\latWidth)$) {{{coredata[N7_content]}}}; % N7
        \node [Assembly, fill=\midenr{coredata[M7_hyper]}] at ($(-4*\latWidth,1*\latWidth)$) {{{coredata[M7_content]}}}; % M7
        \node [Assembly, fill=\lowenr{coredata[L7_hyper]}] at ($(-3*\latWidth,1*\latWidth)$) {{{coredata[L7_content]}}}; % L7
        \node [Assembly, fill=\midenr{coredata[K7_hyper]}] at ($(-2*\latWidth,1*\latWidth)$) {{{coredata[K7_content]}}}; % K7
        \node [Assembly, fill=\lowenr{coredata[J7_hyper]}] at ($(-1*\latWidth,1*\latWidth)$) {{{coredata[J7_content]}}}; % J7
        \node [Assembly, fill=\midenr{coredata[H7_hyper]}] at ($(-0*\latWidth,1*\latWidth)$) {{{coredata[H7_content]}}}; % H7
        \node [Assembly, fill=\lowenr{coredata[G7_hyper]}] at ($( 1*\latWidth,1*\latWidth)$) {{{coredata[G7_content]}}}; % G7
        \node [Assembly, fill=\midenr{coredata[F7_hyper]}] at ($( 2*\latWidth,1*\latWidth)$) {{{coredata[F7_content]}}}; % F7
        \node [Assembly, fill=\lowenr{coredata[E7_hyper]}] at ($( 3*\latWidth,1*\latWidth)$) {{{coredata[E7_content]}}}; % E7
        \node [Assembly, fill=\midenr{coredata[D7_hyper]}] at ($( 4*\latWidth,1*\latWidth)$) {{{coredata[D7_content]}}}; % D7
        \node [Assembly, fill=\lowenr{coredata[C7_hyper]}] at ($( 5*\latWidth,1*\latWidth)$) {{{coredata[C7_content]}}}; % C7
        \node [Assembly, fill=\highenr{coredata[B7_hyper]}] at ($( 6*\latWidth,1*\latWidth)$) {{{coredata[B7_content]}}}; % B7
        \node [Assembly, fill=\highenr{coredata[A7_hyper]}] at ($( 7*\latWidth,1*\latWidth)$) {{{coredata[A7_content]}}}; % A7

        \node [Assembly, fill=\highenr{coredata[R8_hyper]}] at ($(-7*\latWidth,0*\latWidth)$) {{{coredata[R8_content]}}}; % R8
        \node [Assembly, fill=\lowenr{coredata[P8_hyper]}] at ($(-6*\latWidth,0*\latWidth)$) {{{coredata[P8_content]}}}; % P8
        \node [Assembly, fill=\midenr{coredata[N8_hyper]}] at ($(-5*\latWidth,0*\latWidth)$) {{{coredata[N8_content]}}}; % N8
        \node [Assembly, fill=\lowenr{coredata[M8_hyper]}] at ($(-4*\latWidth,0*\latWidth)$) {{{coredata[M8_content]}}}; % M8
        \node [Assembly, fill=\midenr{coredata[L8_hyper]}] at ($(-3*\latWidth,0*\latWidth)$) {{{coredata[L8_content]}}}; % L8
        \node [Assembly, fill=\lowenr{coredata[K8_hyper]}] at ($(-2*\latWidth,0*\latWidth)$) {{{coredata[K8_content]}}}; % K8
        \node [Assembly, fill=\midenr{coredata[J8_hyper]}] at ($(-1*\latWidth,0*\latWidth)$) {{{coredata[J8_content]}}}; % J8
        \node [Assembly, fill=\lowenr{coredata[H8_hyper]}] at ($(-0*\latWidth,0*\latWidth)$) {{{coredata[H8_content]}}}; % H8
        \node [Assembly, fill=\midenr{coredata[G8_hyper]}] at ($( 1*\latWidth,0*\latWidth)$) {{{coredata[G8_content]}}}; % G8
        \node [Assembly, fill=\lowenr{coredata[F8_hyper]}] at ($( 2*\latWidth,0*\latWidth)$) {{{coredata[F8_content]}}}; % F8
        \node [Assembly, fill=\midenr{coredata[E8_hyper]}] at ($( 3*\latWidth,0*\latWidth)$) {{{coredata[E8_content]}}}; % E8
        \node [Assembly, fill=\lowenr{coredata[D8_hyper]}] at ($( 4*\latWidth,0*\latWidth)$) {{{coredata[D8_content]}}}; % D8
        \node [Assembly, fill=\midenr{coredata[C8_hyper]}] at ($( 5*\latWidth,0*\latWidth)$) {{{coredata[C8_content]}}}; % C8
        \node [Assembly, fill=\lowenr{coredata[B8_hyper]}] at ($( 6*\latWidth,0*\latWidth)$) {{{coredata[B8_content]}}}; % B8
        \node [Assembly, fill=\highenr{coredata[A8_hyper]}] at ($( 7*\latWidth,0*\latWidth)$) {{{coredata[A8_content]}}}; % A8

        \node [Assembly, fill=\highenr{coredata[R9_hyper]}] at ($(-7*\latWidth,-1*\latWidth)$) {{{coredata[R9_content]}}}; % R9
        \node [Assembly, fill=\highenr{coredata[P9_hyper]}] at ($(-6*\latWidth,-1*\latWidth)$) {{{coredata[P9_content]}}}; % P9
        \node [Assembly, fill=\lowenr{coredata[N9_hyper]}] at ($(-5*\latWidth,-1*\latWidth)$) {{{coredata[N9_content]}}}; % N9
        \node [Assembly, fill=\midenr{coredata[M9_hyper]}] at ($(-4*\latWidth,-1*\latWidth)$) {{{coredata[M9_content]}}}; % M9
        \node [Assembly, fill=\lowenr{coredata[L9_hyper]}] at ($(-3*\latWidth,-1*\latWidth)$) {{{coredata[L9_content]}}}; % L9
        \node [Assembly, fill=\midenr{coredata[K9_hyper]}] at ($(-2*\latWidth,-1*\latWidth)$) {{{coredata[K9_content]}}}; % K9
        \node [Assembly, fill=\lowenr{coredata[J9_hyper]}] at ($(-1*\latWidth,-1*\latWidth)$) {{{coredata[J9_content]}}}; % J9
        \node [Assembly, fill=\midenr{coredata[H9_hyper]}] at ($(-0*\latWidth,-1*\latWidth)$) {{{coredata[H9_content]}}}; % H9
        \node [Assembly, fill=\lowenr{coredata[G9_hyper]}] at ($( 1*\latWidth,-1*\latWidth)$) {{{coredata[G9_content]}}}; % G9
        \node [Assembly, fill=\midenr{coredata[F9_hyper]}] at ($( 2*\latWidth,-1*\latWidth)$) {{{coredata[F9_content]}}}; % F9
        \node [Assembly, fill=\lowenr{coredata[E9_hyper]}] at ($( 3*\latWidth,-1*\latWidth)$) {{{coredata[E9_content]}}}; % E9
        \node [Assembly, fill=\midenr{coredata[D9_hyper]}] at ($( 4*\latWidth,-1*\latWidth)$) {{{coredata[D9_content]}}}; % D9
        \node [Assembly, fill=\lowenr{coredata[C9_hyper]}] at ($( 5*\latWidth,-1*\latWidth)$) {{{coredata[C9_content]}}}; % C9
        \node [Assembly, fill=\highenr{coredata[B9_hyper]}] at ($( 6*\latWidth,-1*\latWidth)$) {{{coredata[B9_content]}}}; % B9
        \node [Assembly, fill=\highenr{coredata[A9_hyper]}] at ($( 7*\latWidth,-1*\latWidth)$) {{{coredata[A9_content]}}}; % A9

        \node [Assembly, fill=\highenr{coredata[R10_hyper]}] at ($(-7*\latWidth,-2*\latWidth)$) {{{coredata[R10_content]}}}; % R10
        \node [Assembly, fill=\lowenr{coredata[P10_hyper]}] at ($(-6*\latWidth,-2*\latWidth)$) {{{coredata[P10_content]}}}; % P10
        \node [Assembly, fill=\midenr{coredata[N10_hyper]}] at ($(-5*\latWidth,-2*\latWidth)$) {{{coredata[N10_content]}}}; % N10
        \node [Assembly, fill=\lowenr{coredata[M10_hyper]}] at ($(-4*\latWidth,-2*\latWidth)$) {{{coredata[M10_content]}}}; % M10
        \node [Assembly, fill=\midenr{coredata[L10_hyper]}] at ($(-3*\latWidth,-2*\latWidth)$) {{{coredata[L10_content]}}}; % L10
        \node [Assembly, fill=\lowenr{coredata[K10_hyper]}] at ($(-2*\latWidth,-2*\latWidth)$) {{{coredata[K10_content]}}}; % K10
        \node [Assembly, fill=\midenr{coredata[J10_hyper]}] at ($(-1*\latWidth,-2*\latWidth)$) {{{coredata[J10_content]}}}; % J10
        \node [Assembly, fill=\lowenr{coredata[H10_hyper]}] at ($(-0*\latWidth,-2*\latWidth)$) {{{coredata[H10_content]}}}; % H10
        \node [Assembly, fill=\midenr{coredata[G10_hyper]}] at ($( 1*\latWidth,-2*\latWidth)$) {{{coredata[G10_content]}}}; % G10
        \node [Assembly, fill=\lowenr{coredata[F10_hyper]}] at ($( 2*\latWidth,-2*\latWidth)$) {{{coredata[F10_content]}}}; % F10
        \node [Assembly, fill=\midenr{coredata[E10_hyper]}] at ($( 3*\latWidth,-2*\latWidth)$) {{{coredata[E10_content]}}}; % E10
        \node [Assembly, fill=\lowenr{coredata[D10_hyper]}] at ($( 4*\latWidth,-2*\latWidth)$) {{{coredata[D10_content]}}}; % D10
        \node [Assembly, fill=\midenr{coredata[C10_hyper]}] at ($( 5*\latWidth,-2*\latWidth)$) {{{coredata[C10_content]}}}; % C10
        \node [Assembly, fill=\lowenr{coredata[B10_hyper]}] at ($( 6*\latWidth,-2*\latWidth)$) {{{coredata[B10_content]}}}; % B10
        \node [Assembly, fill=\highenr{coredata[A10_hyper]}] at ($( 7*\latWidth,-2*\latWidth)$) {{{coredata[A10_content]}}}; % A10

        \node [Assembly, fill=\highenr{coredata[R11_hyper]}] at ($(-7*\latWidth,-3*\latWidth)$) {{{coredata[R11_content]}}}; % R11
        \node [Assembly, fill=\highenr{coredata[P11_hyper]}] at ($(-6*\latWidth,-3*\latWidth)$) {{{coredata[P11_content]}}}; % P11
        \node [Assembly, fill=\lowenr{coredata[N11_hyper]}] at ($(-5*\latWidth,-3*\latWidth)$) {{{coredata[N11_content]}}}; % N11
        \node [Assembly, fill=\midenr{coredata[M11_hyper]}] at ($(-4*\latWidth,-3*\latWidth)$) {{{coredata[M11_content]}}}; % M11
        \node [Assembly, fill=\lowenr{coredata[L11_hyper]}] at ($(-3*\latWidth,-3*\latWidth)$) {{{coredata[L11_content]}}}; % L11
        \node [Assembly, fill=\midenr{coredata[K11_hyper]}] at ($(-2*\latWidth,-3*\latWidth)$) {{{coredata[K11_content]}}}; % K11
        \node [Assembly, fill=\lowenr{coredata[J11_hyper]}] at ($(-1*\latWidth,-3*\latWidth)$) {{{coredata[J11_content]}}}; % J11
        \node [Assembly, fill=\midenr{coredata[H11_hyper]}] at ($(-0*\latWidth,-3*\latWidth)$) {{{coredata[H11_content]}}}; % H11
        \node [Assembly, fill=\lowenr{coredata[G11_hyper]}] at ($( 1*\latWidth,-3*\latWidth)$) {{{coredata[G11_content]}}}; % G11
        \node [Assembly, fill=\midenr{coredata[F11_hyper]}] at ($( 2*\latWidth,-3*\latWidth)$) {{{coredata[F11_content]}}}; % F11
        \node [Assembly, fill=\lowenr{coredata[E11_hyper]}] at ($( 3*\latWidth,-3*\latWidth)$) {{{coredata[E11_content]}}}; % E11
        \node [Assembly, fill=\midenr{coredata[D11_hyper]}] at ($( 4*\latWidth,-3*\latWidth)$) {{{coredata[D11_content]}}}; % D11
        \node [Assembly, fill=\lowenr{coredata[C11_hyper]}] at ($( 5*\latWidth,-3*\latWidth)$) {{{coredata[C11_content]}}}; % C11
        \node [Assembly, fill=\highenr{coredata[B11_hyper]}] at ($( 6*\latWidth,-3*\latWidth)$) {{{coredata[B11_content]}}}; % B11
        \node [Assembly, fill=\highenr{coredata[A11_hyper]}] at ($( 7*\latWidth,-3*\latWidth)$) {{{coredata[A11_content]}}}; % A11

        \node [Assembly, fill=\highenr{coredata[P12_hyper]}] at ($(-6*\latWidth,-4*\latWidth)$) {{{coredata[P12_content]}}}; % P12
        \node [Assembly, fill=\midenr{coredata[N12_hyper]}] at ($(-5*\latWidth,-4*\latWidth)$) {{{coredata[N12_content]}}}; % N12
        \node [Assembly, fill=\midenr{coredata[M12_hyper]}] at ($(-4*\latWidth,-4*\latWidth)$) {{{coredata[M12_content]}}}; % M12
        \node [Assembly, fill=\midenr{coredata[L12_hyper]}] at ($(-3*\latWidth,-4*\latWidth)$) {{{coredata[L12_content]}}}; % L12
        \node [Assembly, fill=\lowenr{coredata[K12_hyper]}] at ($(-2*\latWidth,-4*\latWidth)$) {{{coredata[K12_content]}}}; % K12
        \node [Assembly, fill=\midenr{coredata[J12_hyper]}] at ($(-1*\latWidth,-4*\latWidth)$) {{{coredata[J12_content]}}}; % J12
        \node [Assembly, fill=\lowenr{coredata[H12_hyper]}] at ($(-0*\latWidth,-4*\latWidth)$) {{{coredata[H12_content]}}}; % H12
        \node [Assembly, fill=\midenr{coredata[G12_hyper]}] at ($( 1*\latWidth,-4*\latWidth)$) {{{coredata[G12_content]}}}; % G12
        \node [Assembly, fill=\lowenr{coredata[F12_hyper]}] at ($( 2*\latWidth,-4*\latWidth)$) {{{coredata[F12_content]}}}; % F12
        \node [Assembly, fill=\midenr{coredata[E12_hyper]}] at ($( 3*\latWidth,-4*\latWidth)$) {{{coredata[E12_content]}}}; % E12
        \node [Assembly, fill=\midenr{coredata[D12_hyper]}] at ($( 4*\latWidth,-4*\latWidth)$) {{{coredata[D12_content]}}}; % D12
        \node [Assembly, fill=\midenr{coredata[C12_hyper]}] at ($( 5*\latWidth,-4*\latWidth)$) {{{coredata[C12_content]}}}; % C12
        \node [Assembly, fill=\highenr{coredata[B12_hyper]}] at ($( 6*\latWidth,-4*\latWidth)$) {{{coredata[B12_content]}}}; % B12

        \node [Assembly, fill=\highenr{coredata[P13_hyper]}] at ($(-6*\latWidth,-5*\latWidth)$) {{{coredata[P13_content]}}}; % P13
        \node [Assembly, fill=\highenr{coredata[N13_hyper]}] at ($(-5*\latWidth,-5*\latWidth)$) {{{coredata[N13_content]}}}; % N13
        \node [Assembly, fill=\midenr{coredata[M13_hyper]}] at ($(-4*\latWidth,-5*\latWidth)$) {{{coredata[M13_content]}}}; % M13
        \node [Assembly, fill=\lowenr{coredata[L13_hyper]}] at ($(-3*\latWidth,-5*\latWidth)$) {{{coredata[L13_content]}}}; % L13
        \node [Assembly, fill=\midenr{coredata[K13_hyper]}] at ($(-2*\latWidth,-5*\latWidth)$) {{{coredata[K13_content]}}}; % K13
        \node [Assembly, fill=\lowenr{coredata[J13_hyper]}] at ($(-1*\latWidth,-5*\latWidth)$) {{{coredata[J13_content]}}}; % J13
        \node [Assembly, fill=\midenr{coredata[H13_hyper]}] at ($(-0*\latWidth,-5*\latWidth)$) {{{coredata[H13_content]}}}; % H13
        \node [Assembly, fill=\lowenr{coredata[G13_hyper]}] at ($( 1*\latWidth,-5*\latWidth)$) {{{coredata[G13_content]}}}; % G13
        \node [Assembly, fill=\midenr{coredata[F13_hyper]}] at ($( 2*\latWidth,-5*\latWidth)$) {{{coredata[F13_content]}}}; % F13
        \node [Assembly, fill=\lowenr{coredata[E13_hyper]}] at ($( 3*\latWidth,-5*\latWidth)$) {{{coredata[E13_content]}}}; % E13
        \node [Assembly, fill=\midenr{coredata[D13_hyper]}] at ($( 4*\latWidth,-5*\latWidth)$) {{{coredata[D13_content]}}}; % D13
        \node [Assembly, fill=\highenr{coredata[C13_hyper]}] at ($( 5*\latWidth,-5*\latWidth)$) {{{coredata[C13_content]}}}; % C13
        \node [Assembly, fill=\highenr{coredata[B13_hyper]}] at ($( 6*\latWidth,-5*\latWidth)$) {{{coredata[B13_content]}}}; % B13

        \node [Assembly, fill=\highenr{coredata[N14_hyper]}] at ($(-5*\latWidth,-6*\latWidth)$) {{{coredata[N14_content]}}}; % N14
        \node [Assembly, fill=\highenr{coredata[M14_hyper]}] at ($(-4*\latWidth,-6*\latWidth)$) {{{coredata[M14_content]}}}; % M14
        \node [Assembly, fill=\highenr{coredata[L14_hyper]}] at ($(-3*\latWidth,-6*\latWidth)$) {{{coredata[L14_content]}}}; % L14
        \node [Assembly, fill=\lowenr{coredata[K14_hyper]}] at ($(-2*\latWidth,-6*\latWidth)$) {{{coredata[K14_content]}}}; % K14
        \node [Assembly, fill=\highenr{coredata[J14_hyper]}] at ($(-1*\latWidth,-6*\latWidth)$) {{{coredata[J14_content]}}}; % J14
        \node [Assembly, fill=\lowenr{coredata[H14_hyper]}] at ($(-0*\latWidth,-6*\latWidth)$) {{{coredata[H14_content]}}}; % H14
        \node [Assembly, fill=\highenr{coredata[G14_hyper]}] at ($( 1*\latWidth,-6*\latWidth)$) {{{coredata[G14_content]}}}; % G14
        \node [Assembly, fill=\lowenr{coredata[F14_hyper]}] at ($( 2*\latWidth,-6*\latWidth)$) {{{coredata[F14_content]}}}; % F14
        \node [Assembly, fill=\highenr{coredata[E14_hyper]}] at ($( 3*\latWidth,-6*\latWidth)$) {{{coredata[E14_content]}}}; % E14
        \node [Assembly, fill=\highenr{coredata[D14_hyper]}] at ($( 4*\latWidth,-6*\latWidth)$) {{{coredata[D14_content]}}}; % D14
        \node [Assembly, fill=\highenr{coredata[C14_hyper]}] at ($( 5*\latWidth,-6*\latWidth)$) {{{coredata[C14_content]}}}; % C14

        \node [Assembly, fill=\highenr{coredata[L15_hyper]}] at ($(-3*\latWidth,-7*\latWidth)$) {{{coredata[L15_content]}}}; % L15
        \node [Assembly, fill=\highenr{coredata[K15_hyper]}] at ($(-2*\latWidth,-7*\latWidth)$) {{{coredata[K15_content]}}}; % K15
        \node [Assembly, fill=\highenr{coredata[J15_hyper]}] at ($(-1*\latWidth,-7*\latWidth)$) {{{coredata[J15_content]}}}; % J15
        \node [Assembly, fill=\highenr{coredata[H15_hyper]}] at ($(-0*\latWidth,-7*\latWidth)$) {{{coredata[H15_content]}}}; % H15
        \node [Assembly, fill=\highenr{coredata[G15_hyper]}] at ($( 1*\latWidth,-7*\latWidth)$) {{{coredata[G15_content]}}}; % G15
        \node [Assembly, fill=\highenr{coredata[F15_hyper]}] at ($( 2*\latWidth,-7*\latWidth)$) {{{coredata[F15_content]}}}; % F15
        \node [Assembly, fill=\highenr{coredata[E15_hyper]}] at ($( 3*\latWidth,-7*\latWidth)$) {{{coredata[E15_content]}}}; % E15

      \end{{tikzpicture}}
    }}

{legend}

    \caption{altcap}{{{caption} \label{{{label}}}}}
\end{{figure}}

"""

quart_fig_t = r"""
\begin{{figure}}[htbp]
    \centering

    % these dimensions are determined in arrow_dimms.ods

    \def\scale{{{scale}}}

    \def\latWidth{{0.2673473684*\scale}}

    \def\RPVOR{{3*\scale}}
    \def\rectW{{0.75*\scale}}
    \def\RPVIR{{2.7315789474*\scale}}
    \def\BarrelIR{{2.3368421053*\scale}}
    \def\BarrelOR{{2.4078947368*\scale}}
    \def\ShieldIR{{2.4223787816*\scale}}
    \def\ShieldOR{{2.5067965189*\scale}}
    \def\LinerIR{{2.7246166598*\scale}}

    \def\bafCIRx{{0.9357157895*\scale}}
    \def\bafCIRy{{2.0051052632*\scale}}
    \def\bafCORx{{0.9633473684*\scale}}
    \def\bafCORy{{2.0327368421*\scale}}
    \def\bafMIRx{{1.7377578947*\scale}}
    \def\bafMIRy{{1.4704105263*\scale}}
    \def\bafMORx{{1.7653894737*\scale}}
    \def\bafMORy{{1.4980421053*\scale}}

    \tikzset{{Assembly/.style={{
        inner sep=0pt,
        text width=\latWidth in,
        minimum size=\latWidth in,
        draw=black,
        align=center
        }}
    }}

    \def\tkzRPV{{(0,0) circle (\RPVIR) (0,0) circle (\RPVOR)}}
    \def\tkzLiner{{(0,0) circle (\LinerIR) (0,0) circle (\RPVIR)}}
    \def\tkzBarrel{{(0,0) circle (\BarrelIR) (0,0) circle (\BarrelOR)}}
    \def\tkzShields{{(0,0) circle (\ShieldIR) (0,0) circle (\ShieldOR)}}

    \def\tkzBaffCOR{{(-\bafCORx, -\bafCORy) rectangle (\bafCORx, \bafCORy)}}
    \def\tkzBaffCIR{{(-\bafCIRx, -\bafCIRy) rectangle (\bafCIRx, \bafCIRy)}}
    \def\tkzBaffMOR{{(-\bafMORx, -\bafMORy) rectangle (\bafMORx, \bafMORy)}}
    \def\tkzBaffMIR{{(-\bafMIRx, -\bafMIRy) rectangle (\bafMIRx, \bafMIRy) }}
    \def\tkzBaffleC{{ \tkzBaffCIR \tkzBaffCOR }}
    \def\tkzBaffleM{{ \tkzBaffMIR \tkzBaffMOR }}

    \def\tkzBaffCClip{{\tkzBaffCIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}
    \def\tkzBaffMClip{{\tkzBaffMIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}

    \def\highenr{{blue!50}}
    \def\midenr{{yellow!50}}
    \def\lowenr{{red!50}}

    \scalebox{{{scalebox}}}{{

      \begin{{tikzpicture}}[x=1in,y=1in]

        {struct}\begin{{scope}}
          {struct}\clip ($(-\latWidth/2,\latWidth/2)$) rectangle (\RPVOR,-\RPVOR);
          % draw RPV, barrel, and shield panels

          {struct}\path[fill=black!90!white,even odd rule] \tkzRPV;
          {struct}\path[fill=black,even odd rule] \tkzLiner;
          {struct}\path[fill=black,even odd rule] \tkzBarrel;
          {struct}\begin{{scope}}
          {struct}  \clip (0,0) -- +(61:\RPVOR) arc (61:29:\RPVOR) --
          {struct}        (0,0) -- +(151:\RPVOR) arc (151:119:\RPVOR) --
          {struct}        (0,0) -- +(241:\RPVOR) arc (241:209:\RPVOR) --
          {struct}        (0,0) -- +(331:\RPVOR) arc (331:299:\RPVOR) -- cycle;
          {struct}  \path[fill=black,even odd rule] \tkzShields;
          {struct}\end{{scope}}

          % draw baffle north/south

          {struct}\begin{{scope}}[even odd rule]
          {struct}  \clip[rotate=90] \tkzBaffMClip;
          {struct}  \path[fill=black] \tkzBaffleC;
          {struct}\end{{scope}}
          {struct}\begin{{scope}}[even odd rule]
          {struct}  \clip \tkzBaffCClip;
          {struct}  \clip \tkzBaffMClip;
          {struct}  \path[fill=black, rotate=90] \tkzBaffleM;
          {struct}\end{{scope}}

          % draw baffle east/west

          {struct}\begin{{scope}}[rotate=90]
          {struct}  \begin{{scope}}[even odd rule]
          {struct}    \clip[rotate=90] \tkzBaffMClip;
          {struct}    \path[fill=black] \tkzBaffleC;
          {struct}  \end{{scope}}
          {struct}  \begin{{scope}}[even odd rule]
          {struct}    \clip \tkzBaffCClip;
          {struct}    \clip \tkzBaffMClip;
          {struct}    \path[fill=black, rotate=90] \tkzBaffleM;
          {struct}  \end{{scope}}
          {struct}\end{{scope}}

        {struct}\end{{scope}}

        % draw assembly row/column headers

        \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{H}} -- ($(-0*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{G}} -- ($(1*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{F}} -- ($(2*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{E}} -- ($(3*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{D}} -- ($(4*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{C}} -- ($(5*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{B}} -- ($(6*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{A}} -- ($(7*\latWidth,{head_llm}*\latWidth)$);

        \begin{{scope}}[rotate=90]
          \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{15}} -- ($(-7*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{14}} -- ($(-6*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{13}} -- ($(-5*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{12}} -- ($(-4*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{11}} -- ($(-3*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{10}} -- ($(-2*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{9}} -- ($(-1*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{8}} -- ($(-0*\latWidth,{head_llm}*\latWidth)$);
        \end{{scope}}

        % draw fuel assembly nodes

        \node [Assembly, fill=\lowenr{coredata[H8_hyper]}] at ($(-0*\latWidth,0*\latWidth)$) {{{coredata[H8_content]}}}; % H8
        \node [Assembly, fill=\midenr{coredata[G8_hyper]}] at ($( 1*\latWidth,0*\latWidth)$) {{{coredata[G8_content]}}}; % G8
        \node [Assembly, fill=\lowenr{coredata[F8_hyper]}] at ($( 2*\latWidth,0*\latWidth)$) {{{coredata[F8_content]}}}; % F8
        \node [Assembly, fill=\midenr{coredata[E8_hyper]}] at ($( 3*\latWidth,0*\latWidth)$) {{{coredata[E8_content]}}}; % E8
        \node [Assembly, fill=\lowenr{coredata[D8_hyper]}] at ($( 4*\latWidth,0*\latWidth)$) {{{coredata[D8_content]}}}; % D8
        \node [Assembly, fill=\midenr{coredata[C8_hyper]}] at ($( 5*\latWidth,0*\latWidth)$) {{{coredata[C8_content]}}}; % C8
        \node [Assembly, fill=\lowenr{coredata[B8_hyper]}] at ($( 6*\latWidth,0*\latWidth)$) {{{coredata[B8_content]}}}; % B8
        \node [Assembly, fill=\highenr{coredata[A8_hyper]}] at ($( 7*\latWidth,0*\latWidth)$) {{{coredata[A8_content]}}}; % A8

        \node [Assembly, fill=\midenr{coredata[H9_hyper]}] at ($(-0*\latWidth,-1*\latWidth)$) {{{coredata[H9_content]}}}; % H9
        \node [Assembly, fill=\lowenr{coredata[G9_hyper]}] at ($( 1*\latWidth,-1*\latWidth)$) {{{coredata[G9_content]}}}; % G9
        \node [Assembly, fill=\midenr{coredata[F9_hyper]}] at ($( 2*\latWidth,-1*\latWidth)$) {{{coredata[F9_content]}}}; % F9
        \node [Assembly, fill=\lowenr{coredata[E9_hyper]}] at ($( 3*\latWidth,-1*\latWidth)$) {{{coredata[E9_content]}}}; % E9
        \node [Assembly, fill=\midenr{coredata[D9_hyper]}] at ($( 4*\latWidth,-1*\latWidth)$) {{{coredata[D9_content]}}}; % D9
        \node [Assembly, fill=\lowenr{coredata[C9_hyper]}] at ($( 5*\latWidth,-1*\latWidth)$) {{{coredata[C9_content]}}}; % C9
        \node [Assembly, fill=\highenr{coredata[B9_hyper]}] at ($( 6*\latWidth,-1*\latWidth)$) {{{coredata[B9_content]}}}; % B9
        \node [Assembly, fill=\highenr{coredata[A9_hyper]}] at ($( 7*\latWidth,-1*\latWidth)$) {{{coredata[A9_content]}}}; % A9

        \node [Assembly, fill=\lowenr{coredata[H10_hyper]}] at ($(-0*\latWidth,-2*\latWidth)$) {{{coredata[H10_content]}}}; % H10
        \node [Assembly, fill=\midenr{coredata[G10_hyper]}] at ($( 1*\latWidth,-2*\latWidth)$) {{{coredata[G10_content]}}}; % G10
        \node [Assembly, fill=\lowenr{coredata[F10_hyper]}] at ($( 2*\latWidth,-2*\latWidth)$) {{{coredata[F10_content]}}}; % F10
        \node [Assembly, fill=\midenr{coredata[E10_hyper]}] at ($( 3*\latWidth,-2*\latWidth)$) {{{coredata[E10_content]}}}; % E10
        \node [Assembly, fill=\lowenr{coredata[D10_hyper]}] at ($( 4*\latWidth,-2*\latWidth)$) {{{coredata[D10_content]}}}; % D10
        \node [Assembly, fill=\midenr{coredata[C10_hyper]}] at ($( 5*\latWidth,-2*\latWidth)$) {{{coredata[C10_content]}}}; % C10
        \node [Assembly, fill=\lowenr{coredata[B10_hyper]}] at ($( 6*\latWidth,-2*\latWidth)$) {{{coredata[B10_content]}}}; % B10
        \node [Assembly, fill=\highenr{coredata[A10_hyper]}] at ($( 7*\latWidth,-2*\latWidth)$) {{{coredata[A10_content]}}}; % A10

        \node [Assembly, fill=\midenr{coredata[H11_hyper]}] at ($(-0*\latWidth,-3*\latWidth)$) {{{coredata[H11_content]}}}; % H11
        \node [Assembly, fill=\lowenr{coredata[G11_hyper]}] at ($( 1*\latWidth,-3*\latWidth)$) {{{coredata[G11_content]}}}; % G11
        \node [Assembly, fill=\midenr{coredata[F11_hyper]}] at ($( 2*\latWidth,-3*\latWidth)$) {{{coredata[F11_content]}}}; % F11
        \node [Assembly, fill=\lowenr{coredata[E11_hyper]}] at ($( 3*\latWidth,-3*\latWidth)$) {{{coredata[E11_content]}}}; % E11
        \node [Assembly, fill=\midenr{coredata[D11_hyper]}] at ($( 4*\latWidth,-3*\latWidth)$) {{{coredata[D11_content]}}}; % D11
        \node [Assembly, fill=\lowenr{coredata[C11_hyper]}] at ($( 5*\latWidth,-3*\latWidth)$) {{{coredata[C11_content]}}}; % C11
        \node [Assembly, fill=\highenr{coredata[B11_hyper]}] at ($( 6*\latWidth,-3*\latWidth)$) {{{coredata[B11_content]}}}; % B11
        \node [Assembly, fill=\highenr{coredata[A11_hyper]}] at ($( 7*\latWidth,-3*\latWidth)$) {{{coredata[A11_content]}}}; % A11

        \node [Assembly, fill=\lowenr{coredata[H12_hyper]}] at ($(-0*\latWidth,-4*\latWidth)$) {{{coredata[H12_content]}}}; % H12
        \node [Assembly, fill=\midenr{coredata[G12_hyper]}] at ($( 1*\latWidth,-4*\latWidth)$) {{{coredata[G12_content]}}}; % G12
        \node [Assembly, fill=\lowenr{coredata[F12_hyper]}] at ($( 2*\latWidth,-4*\latWidth)$) {{{coredata[F12_content]}}}; % F12
        \node [Assembly, fill=\midenr{coredata[E12_hyper]}] at ($( 3*\latWidth,-4*\latWidth)$) {{{coredata[E12_content]}}}; % E12
        \node [Assembly, fill=\midenr{coredata[D12_hyper]}] at ($( 4*\latWidth,-4*\latWidth)$) {{{coredata[D12_content]}}}; % D12
        \node [Assembly, fill=\midenr{coredata[C12_hyper]}] at ($( 5*\latWidth,-4*\latWidth)$) {{{coredata[C12_content]}}}; % C12
        \node [Assembly, fill=\highenr{coredata[B12_hyper]}] at ($( 6*\latWidth,-4*\latWidth)$) {{{coredata[B12_content]}}}; % B12

        \node [Assembly, fill=\midenr{coredata[H13_hyper]}] at ($(-0*\latWidth,-5*\latWidth)$) {{{coredata[H13_content]}}}; % H13
        \node [Assembly, fill=\lowenr{coredata[G13_hyper]}] at ($( 1*\latWidth,-5*\latWidth)$) {{{coredata[G13_content]}}}; % G13
        \node [Assembly, fill=\midenr{coredata[F13_hyper]}] at ($( 2*\latWidth,-5*\latWidth)$) {{{coredata[F13_content]}}}; % F13
        \node [Assembly, fill=\lowenr{coredata[E13_hyper]}] at ($( 3*\latWidth,-5*\latWidth)$) {{{coredata[E13_content]}}}; % E13
        \node [Assembly, fill=\midenr{coredata[D13_hyper]}] at ($( 4*\latWidth,-5*\latWidth)$) {{{coredata[D13_content]}}}; % D13
        \node [Assembly, fill=\highenr{coredata[C13_hyper]}] at ($( 5*\latWidth,-5*\latWidth)$) {{{coredata[C13_content]}}}; % C13
        \node [Assembly, fill=\highenr{coredata[B13_hyper]}] at ($( 6*\latWidth,-5*\latWidth)$) {{{coredata[B13_content]}}}; % B13

        \node [Assembly, fill=\lowenr{coredata[H14_hyper]}] at ($(-0*\latWidth,-6*\latWidth)$) {{{coredata[H14_content]}}}; % H14
        \node [Assembly, fill=\highenr{coredata[G14_hyper]}] at ($( 1*\latWidth,-6*\latWidth)$) {{{coredata[G14_content]}}}; % G14
        \node [Assembly, fill=\lowenr{coredata[F14_hyper]}] at ($( 2*\latWidth,-6*\latWidth)$) {{{coredata[F14_content]}}}; % F14
        \node [Assembly, fill=\highenr{coredata[E14_hyper]}] at ($( 3*\latWidth,-6*\latWidth)$) {{{coredata[E14_content]}}}; % E14
        \node [Assembly, fill=\highenr{coredata[D14_hyper]}] at ($( 4*\latWidth,-6*\latWidth)$) {{{coredata[D14_content]}}}; % D14
        \node [Assembly, fill=\highenr{coredata[C14_hyper]}] at ($( 5*\latWidth,-6*\latWidth)$) {{{coredata[C14_content]}}}; % C14

        \node [Assembly, fill=\highenr{coredata[H15_hyper]}] at ($(-0*\latWidth,-7*\latWidth)$) {{{coredata[H15_content]}}}; % H15
        \node [Assembly, fill=\highenr{coredata[G15_hyper]}] at ($( 1*\latWidth,-7*\latWidth)$) {{{coredata[G15_content]}}}; % G15
        \node [Assembly, fill=\highenr{coredata[F15_hyper]}] at ($( 2*\latWidth,-7*\latWidth)$) {{{coredata[F15_content]}}}; % F15
        \node [Assembly, fill=\highenr{coredata[E15_hyper]}] at ($( 3*\latWidth,-7*\latWidth)$) {{{coredata[E15_content]}}}; % E15

      \end{{tikzpicture}}
    }}

{legend}

    \caption{altcap}{{{caption} \label{{{label}}}}}
\end{{figure}}

"""


main_fig_t_c2 = r"""
\begin{{figure}}[htbp]
    \centering

    % these dimensions are determined in arrow_dimms.ods

    \def\scale{{{scale}}}

    \def\latWidth{{0.2673473684*\scale}}

    \def\RPVOR{{3*\scale}}
    \def\rectW{{0.75*\scale}}
    \def\RPVIR{{2.7315789474*\scale}}
    \def\BarrelIR{{2.3368421053*\scale}}
    \def\BarrelOR{{2.4078947368*\scale}}
    \def\ShieldIR{{2.4223787816*\scale}}
    \def\ShieldOR{{2.5067965189*\scale}}
    \def\LinerIR{{2.7246166598*\scale}}

    \def\bafCIRx{{0.9357157895*\scale}}
    \def\bafCIRy{{2.0051052632*\scale}}
    \def\bafCORx{{0.9633473684*\scale}}
    \def\bafCORy{{2.0327368421*\scale}}
    \def\bafMIRx{{1.7377578947*\scale}}
    \def\bafMIRy{{1.4704105263*\scale}}
    \def\bafMORx{{1.7653894737*\scale}}
    \def\bafMORy{{1.4980421053*\scale}}

    \tikzset{{Assembly/.style={{
        inner sep=0pt,
        text width=\latWidth in,
        minimum size=\latWidth in,
        draw=black,
        align=center
        }}
    }}

    \def\tkzRPV{{(0,0) circle (\RPVIR) (0,0) circle (\RPVOR)}}
    \def\tkzLiner{{(0,0) circle (\LinerIR) (0,0) circle (\RPVIR)}}
    \def\tkzBarrel{{(0,0) circle (\BarrelIR) (0,0) circle (\BarrelOR)}}
    \def\tkzShields{{(0,0) circle (\ShieldIR) (0,0) circle (\ShieldOR)}}

    \def\tkzBaffCOR{{(-\bafCORx, -\bafCORy) rectangle (\bafCORx, \bafCORy)}}
    \def\tkzBaffCIR{{(-\bafCIRx, -\bafCIRy) rectangle (\bafCIRx, \bafCIRy)}}
    \def\tkzBaffMOR{{(-\bafMORx, -\bafMORy) rectangle (\bafMORx, \bafMORy)}}
    \def\tkzBaffMIR{{(-\bafMIRx, -\bafMIRy) rectangle (\bafMIRx, \bafMIRy) }}
    \def\tkzBaffleC{{ \tkzBaffCIR \tkzBaffCOR }}
    \def\tkzBaffleM{{ \tkzBaffMIR \tkzBaffMOR }}

    \def\tkzBaffCClip{{\tkzBaffCIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}
    \def\tkzBaffMClip{{\tkzBaffMIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}

    \def\noenr{{black!10}}
    \def\lowenr{{green!60!black}}
    \def\highenr{{orange!90}}

    \scalebox{{{scalebox}}}{{

      \begin{{tikzpicture}}[x=1in,y=1in]

        % draw RPV, barrel, and shield panels

        {struct}\path[fill=black!90!white,even odd rule] \tkzRPV;
        {struct}\path[fill=black,even odd rule] \tkzLiner;
        {struct}\path[fill=black,even odd rule] \tkzBarrel;
        {struct}\begin{{scope}}
        {struct}  \clip (0,0) -- +(61:\RPVOR) arc (61:29:\RPVOR) --
        {struct}        (0,0) -- +(151:\RPVOR) arc (151:119:\RPVOR) --
        {struct}        (0,0) -- +(241:\RPVOR) arc (241:209:\RPVOR) --
        {struct}        (0,0) -- +(331:\RPVOR) arc (331:299:\RPVOR) -- cycle;
        {struct}  \path[fill=black,even odd rule] \tkzShields;
        {struct}\end{{scope}}

        % draw baffle north/south

        {struct}\begin{{scope}}[even odd rule]
        {struct}  \clip[rotate=90] \tkzBaffMClip;
        {struct}  \path[fill=black] \tkzBaffleC;
        {struct}\end{{scope}}
        {struct}\begin{{scope}}[even odd rule]
        {struct}  \clip \tkzBaffCClip;
        {struct}  \clip \tkzBaffMClip;
        {struct}  \path[fill=black, rotate=90] \tkzBaffleM;
        {struct}\end{{scope}}

        % draw baffle east/west

        {struct}\begin{{scope}}[rotate=90]
        {struct}  \begin{{scope}}[even odd rule]
        {struct}    \clip[rotate=90] \tkzBaffMClip;
        {struct}    \path[fill=black] \tkzBaffleC;
        {struct}  \end{{scope}}
        {struct}  \begin{{scope}}[even odd rule]
        {struct}    \clip \tkzBaffCClip;
        {struct}    \clip \tkzBaffMClip;
        {struct}    \path[fill=black, rotate=90] \tkzBaffleM;
        {struct}  \end{{scope}}
        {struct}\end{{scope}}

        % draw assembly row/column headers

        \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{R}} -- ($(-7*\latWidth,4*\latWidth)$);
        \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{P}} -- ($(-6*\latWidth,6*\latWidth)$);
        \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{N}} -- ($(-5*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{M}} -- ($(-4*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{L}} -- ($(-3*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{K}} -- ($(-2*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{J}} -- ($(-1*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{H}} -- ($(-0*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{G}} -- ($(1*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{F}} -- ($(2*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{E}} -- ($(3*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{D}} -- ($(4*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{C}} -- ($(5*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{B}} -- ($(6*\latWidth,6*\latWidth)$);
        \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{A}} -- ($(7*\latWidth,4*\latWidth)$);

        \begin{{scope}}[rotate=90]
          \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{15}} -- ($(-7*\latWidth,4*\latWidth)$);
          \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{14}} -- ($(-6*\latWidth,6*\latWidth)$);
          \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{13}} -- ($(-5*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{12}} -- ($(-4*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{11}} -- ($(-3*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{10}} -- ($(-2*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{9}} -- ($(-1*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{8}} -- ($(-0*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{7}} -- ($(1*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{6}} -- ($(2*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{5}} -- ($(3*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{4}} -- ($(4*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{3}} -- ($(5*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{2}} -- ($(6*\latWidth,6*\latWidth)$);
          \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{1}} -- ($(7*\latWidth,4*\latWidth)$);
        \end{{scope}}

        % draw fuel assembly nodes

        \node [Assembly, fill=\noenr{coredata[L1_hyper]}] at ($(-3*\latWidth,7*\latWidth)$) {{{coredata[L1_content]}}}; % L1
        \node [Assembly, fill=\highenr{coredata[K1_hyper]}] at ($(-2*\latWidth,7*\latWidth)$) {{{coredata[K1_content]}}}; % K1
        \node [Assembly, fill=\lowenr{coredata[J1_hyper]}] at ($(-1*\latWidth,7*\latWidth)$) {{{coredata[J1_content]}}}; % J1
        \node [Assembly, fill=\highenr{coredata[H1_hyper]}] at ($(-0*\latWidth,7*\latWidth)$) {{{coredata[H1_content]}}}; % H1
        \node [Assembly, fill=\lowenr{coredata[G1_hyper]}] at ($( 1*\latWidth,7*\latWidth)$) {{{coredata[G1_content]}}}; % G1
        \node [Assembly, fill=\highenr{coredata[F1_hyper]}] at ($( 2*\latWidth,7*\latWidth)$) {{{coredata[F1_content]}}}; % F1
        \node [Assembly, fill=\noenr{coredata[E1_hyper]}] at ($( 3*\latWidth,7*\latWidth)$) {{{coredata[E1_content]}}}; % E1

        \node [Assembly, fill=\noenr{coredata[N2_hyper]}] at ($(-5*\latWidth,6*\latWidth)$) {{{coredata[N2_content]}}}; % N2
        \node [Assembly, fill=\lowenr{coredata[M2_hyper]}] at ($(-4*\latWidth,6*\latWidth)$) {{{coredata[M2_content]}}}; % M2
        \node [Assembly, fill=\lowenr{coredata[L2_hyper]}] at ($(-3*\latWidth,6*\latWidth)$) {{{coredata[L2_content]}}}; % L2
        \node [Assembly, fill=\noenr{coredata[K2_hyper]}] at ($(-2*\latWidth,6*\latWidth)$) {{{coredata[K2_content]}}}; % K2
        \node [Assembly, fill=\noenr{coredata[J2_hyper]}] at ($(-1*\latWidth,6*\latWidth)$) {{{coredata[J2_content]}}}; % J2
        \node [Assembly, fill=\noenr{coredata[H2_hyper]}] at ($(-0*\latWidth,6*\latWidth)$) {{{coredata[H2_content]}}}; % H2
        \node [Assembly, fill=\noenr{coredata[G2_hyper]}] at ($( 1*\latWidth,6*\latWidth)$) {{{coredata[G2_content]}}}; % G2
        \node [Assembly, fill=\noenr{coredata[F2_hyper]}] at ($( 2*\latWidth,6*\latWidth)$) {{{coredata[F2_content]}}}; % F2
        \node [Assembly, fill=\lowenr{coredata[E2_hyper]}] at ($( 3*\latWidth,6*\latWidth)$) {{{coredata[E2_content]}}}; % E2
        \node [Assembly, fill=\lowenr{coredata[D2_hyper]}] at ($( 4*\latWidth,6*\latWidth)$) {{{coredata[D2_content]}}}; % D2
        \node [Assembly, fill=\noenr{coredata[C2_hyper]}] at ($( 5*\latWidth,6*\latWidth)$) {{{coredata[C2_content]}}}; % C2

        \node [Assembly, fill=\noenr{coredata[P3_hyper]}] at ($(-6*\latWidth,5*\latWidth)$) {{{coredata[P3_content]}}}; % P3
        \node [Assembly, fill=\highenr{coredata[N3_hyper]}] at ($(-5*\latWidth,5*\latWidth)$) {{{coredata[N3_content]}}}; % N3
        \node [Assembly, fill=\noenr{coredata[M3_hyper]}] at ($(-4*\latWidth,5*\latWidth)$) {{{coredata[M3_content]}}}; % M3
        \node [Assembly, fill=\noenr{coredata[L3_hyper]}] at ($(-3*\latWidth,5*\latWidth)$) {{{coredata[L3_content]}}}; % L3
        \node [Assembly, fill=\lowenr{coredata[K3_hyper]}] at ($(-2*\latWidth,5*\latWidth)$) {{{coredata[K3_content]}}}; % K3
        \node [Assembly, fill=\noenr{coredata[J3_hyper]}] at ($(-1*\latWidth,5*\latWidth)$) {{{coredata[J3_content]}}}; % J3
        \node [Assembly, fill=\noenr{coredata[H3_hyper]}] at ($(-0*\latWidth,5*\latWidth)$) {{{coredata[H3_content]}}}; % H3
        \node [Assembly, fill=\noenr{coredata[G3_hyper]}] at ($( 1*\latWidth,5*\latWidth)$) {{{coredata[G3_content]}}}; % G3
        \node [Assembly, fill=\lowenr{coredata[F3_hyper]}] at ($( 2*\latWidth,5*\latWidth)$) {{{coredata[F3_content]}}}; % F3
        \node [Assembly, fill=\noenr{coredata[E3_hyper]}] at ($( 3*\latWidth,5*\latWidth)$) {{{coredata[E3_content]}}}; % E3
        \node [Assembly, fill=\noenr{coredata[D3_hyper]}] at ($( 4*\latWidth,5*\latWidth)$) {{{coredata[D3_content]}}}; % D3
        \node [Assembly, fill=\highenr{coredata[C3_hyper]}] at ($( 5*\latWidth,5*\latWidth)$) {{{coredata[C3_content]}}}; % C3
        \node [Assembly, fill=\noenr{coredata[B3_hyper]}] at ($( 6*\latWidth,5*\latWidth)$) {{{coredata[B3_content]}}}; % B3

        \node [Assembly, fill=\lowenr{coredata[P4_hyper]}] at ($(-6*\latWidth,4*\latWidth)$) {{{coredata[P4_content]}}}; % P4
        \node [Assembly, fill=\noenr{coredata[N4_hyper]}] at ($(-5*\latWidth,4*\latWidth)$) {{{coredata[N4_content]}}}; % N4
        \node [Assembly, fill=\noenr{coredata[M4_hyper]}] at ($(-4*\latWidth,4*\latWidth)$) {{{coredata[M4_content]}}}; % M4
        \node [Assembly, fill=\lowenr{coredata[L4_hyper]}] at ($(-3*\latWidth,4*\latWidth)$) {{{coredata[L4_content]}}}; % L4
        \node [Assembly, fill=\noenr{coredata[K4_hyper]}] at ($(-2*\latWidth,4*\latWidth)$) {{{coredata[K4_content]}}}; % K4
        \node [Assembly, fill=\noenr{coredata[J4_hyper]}] at ($(-1*\latWidth,4*\latWidth)$) {{{coredata[J4_content]}}}; % J4
        \node [Assembly, fill=\noenr{coredata[H4_hyper]}] at ($(-0*\latWidth,4*\latWidth)$) {{{coredata[H4_content]}}}; % H4
        \node [Assembly, fill=\noenr{coredata[G4_hyper]}] at ($( 1*\latWidth,4*\latWidth)$) {{{coredata[G4_content]}}}; % G4
        \node [Assembly, fill=\noenr{coredata[F4_hyper]}] at ($( 2*\latWidth,4*\latWidth)$) {{{coredata[F4_content]}}}; % F4
        \node [Assembly, fill=\lowenr{coredata[E4_hyper]}] at ($( 3*\latWidth,4*\latWidth)$) {{{coredata[E4_content]}}}; % E4
        \node [Assembly, fill=\noenr{coredata[D4_hyper]}] at ($( 4*\latWidth,4*\latWidth)$) {{{coredata[D4_content]}}}; % D4
        \node [Assembly, fill=\noenr{coredata[C4_hyper]}] at ($( 5*\latWidth,4*\latWidth)$) {{{coredata[C4_content]}}}; % C4
        \node [Assembly, fill=\lowenr{coredata[B4_hyper]}] at ($( 6*\latWidth,4*\latWidth)$) {{{coredata[B4_content]}}}; % B4

        \node [Assembly, fill=\noenr{coredata[R5_hyper]}] at ($(-7*\latWidth,3*\latWidth)$) {{{coredata[R5_content]}}}; % R5
        \node [Assembly, fill=\lowenr{coredata[P5_hyper]}] at ($(-6*\latWidth,3*\latWidth)$) {{{coredata[P5_content]}}}; % P5
        \node [Assembly, fill=\noenr{coredata[N5_hyper]}] at ($(-5*\latWidth,3*\latWidth)$) {{{coredata[N5_content]}}}; % N5
        \node [Assembly, fill=\lowenr{coredata[M5_hyper]}] at ($(-4*\latWidth,3*\latWidth)$) {{{coredata[M5_content]}}}; % M5
        \node [Assembly, fill=\noenr{coredata[L5_hyper]}] at ($(-3*\latWidth,3*\latWidth)$) {{{coredata[L5_content]}}}; % L5
        \node [Assembly, fill=\lowenr{coredata[K5_hyper]}] at ($(-2*\latWidth,3*\latWidth)$) {{{coredata[K5_content]}}}; % K5
        \node [Assembly, fill=\noenr{coredata[J5_hyper]}] at ($(-1*\latWidth,3*\latWidth)$) {{{coredata[J5_content]}}}; % J5
        \node [Assembly, fill=\noenr{coredata[H5_hyper]}] at ($(-0*\latWidth,3*\latWidth)$) {{{coredata[H5_content]}}}; % H5
        \node [Assembly, fill=\noenr{coredata[G5_hyper]}] at ($( 1*\latWidth,3*\latWidth)$) {{{coredata[G5_content]}}}; % G5
        \node [Assembly, fill=\lowenr{coredata[F5_hyper]}] at ($( 2*\latWidth,3*\latWidth)$) {{{coredata[F5_content]}}}; % F5
        \node [Assembly, fill=\noenr{coredata[E5_hyper]}] at ($( 3*\latWidth,3*\latWidth)$) {{{coredata[E5_content]}}}; % E5
        \node [Assembly, fill=\lowenr{coredata[D5_hyper]}] at ($( 4*\latWidth,3*\latWidth)$) {{{coredata[D5_content]}}}; % D5
        \node [Assembly, fill=\noenr{coredata[C5_hyper]}] at ($( 5*\latWidth,3*\latWidth)$) {{{coredata[C5_content]}}}; % C5
        \node [Assembly, fill=\lowenr{coredata[B5_hyper]}] at ($( 6*\latWidth,3*\latWidth)$) {{{coredata[B5_content]}}}; % B5
        \node [Assembly, fill=\noenr{coredata[A5_hyper]}] at ($( 7*\latWidth,3*\latWidth)$) {{{coredata[A5_content]}}}; % A5

        \node [Assembly, fill=\highenr{coredata[R6_hyper]}] at ($(-7*\latWidth,2*\latWidth)$) {{{coredata[R6_content]}}}; % R6
        \node [Assembly, fill=\noenr{coredata[P6_hyper]}] at ($(-6*\latWidth,2*\latWidth)$) {{{coredata[P6_content]}}}; % P6
        \node [Assembly, fill=\lowenr{coredata[N6_hyper]}] at ($(-5*\latWidth,2*\latWidth)$) {{{coredata[N6_content]}}}; % N6
        \node [Assembly, fill=\noenr{coredata[M6_hyper]}] at ($(-4*\latWidth,2*\latWidth)$) {{{coredata[M6_content]}}}; % M6
        \node [Assembly, fill=\lowenr{coredata[L6_hyper]}] at ($(-3*\latWidth,2*\latWidth)$) {{{coredata[L6_content]}}}; % L6
        \node [Assembly, fill=\noenr{coredata[K6_hyper]}] at ($(-2*\latWidth,2*\latWidth)$) {{{coredata[K6_content]}}}; % K6
        \node [Assembly, fill=\noenr{coredata[J6_hyper]}] at ($(-1*\latWidth,2*\latWidth)$) {{{coredata[J6_content]}}}; % J6
        \node [Assembly, fill=\noenr{coredata[H6_hyper]}] at ($(-0*\latWidth,2*\latWidth)$) {{{coredata[H6_content]}}}; % H6
        \node [Assembly, fill=\noenr{coredata[G6_hyper]}] at ($( 1*\latWidth,2*\latWidth)$) {{{coredata[G6_content]}}}; % G6
        \node [Assembly, fill=\noenr{coredata[F6_hyper]}] at ($( 2*\latWidth,2*\latWidth)$) {{{coredata[F6_content]}}}; % F6
        \node [Assembly, fill=\lowenr{coredata[E6_hyper]}] at ($( 3*\latWidth,2*\latWidth)$) {{{coredata[E6_content]}}}; % E6
        \node [Assembly, fill=\noenr{coredata[D6_hyper]}] at ($( 4*\latWidth,2*\latWidth)$) {{{coredata[D6_content]}}}; % D6
        \node [Assembly, fill=\lowenr{coredata[C6_hyper]}] at ($( 5*\latWidth,2*\latWidth)$) {{{coredata[C6_content]}}}; % C6
        \node [Assembly, fill=\noenr{coredata[B6_hyper]}] at ($( 6*\latWidth,2*\latWidth)$) {{{coredata[B6_content]}}}; % B6
        \node [Assembly, fill=\highenr{coredata[A6_hyper]}] at ($( 7*\latWidth,2*\latWidth)$) {{{coredata[A6_content]}}}; % A6

        \node [Assembly, fill=\lowenr{coredata[R7_hyper]}] at ($(-7*\latWidth,1*\latWidth)$) {{{coredata[R7_content]}}}; % R7
        \node [Assembly, fill=\noenr{coredata[P7_hyper]}] at ($(-6*\latWidth,1*\latWidth)$) {{{coredata[P7_content]}}}; % P7
        \node [Assembly, fill=\noenr{coredata[N7_hyper]}] at ($(-5*\latWidth,1*\latWidth)$) {{{coredata[N7_content]}}}; % N7
        \node [Assembly, fill=\noenr{coredata[M7_hyper]}] at ($(-4*\latWidth,1*\latWidth)$) {{{coredata[M7_content]}}}; % M7
        \node [Assembly, fill=\noenr{coredata[L7_hyper]}] at ($(-3*\latWidth,1*\latWidth)$) {{{coredata[L7_content]}}}; % L7
        \node [Assembly, fill=\noenr{coredata[K7_hyper]}] at ($(-2*\latWidth,1*\latWidth)$) {{{coredata[K7_content]}}}; % K7
        \node [Assembly, fill=\noenr{coredata[J7_hyper]}] at ($(-1*\latWidth,1*\latWidth)$) {{{coredata[J7_content]}}}; % J7
        \node [Assembly, fill=\noenr{coredata[H7_hyper]}] at ($(-0*\latWidth,1*\latWidth)$) {{{coredata[H7_content]}}}; % H7
        \node [Assembly, fill=\noenr{coredata[G7_hyper]}] at ($( 1*\latWidth,1*\latWidth)$) {{{coredata[G7_content]}}}; % G7
        \node [Assembly, fill=\noenr{coredata[F7_hyper]}] at ($( 2*\latWidth,1*\latWidth)$) {{{coredata[F7_content]}}}; % F7
        \node [Assembly, fill=\noenr{coredata[E7_hyper]}] at ($( 3*\latWidth,1*\latWidth)$) {{{coredata[E7_content]}}}; % E7
        \node [Assembly, fill=\noenr{coredata[D7_hyper]}] at ($( 4*\latWidth,1*\latWidth)$) {{{coredata[D7_content]}}}; % D7
        \node [Assembly, fill=\noenr{coredata[C7_hyper]}] at ($( 5*\latWidth,1*\latWidth)$) {{{coredata[C7_content]}}}; % C7
        \node [Assembly, fill=\noenr{coredata[B7_hyper]}] at ($( 6*\latWidth,1*\latWidth)$) {{{coredata[B7_content]}}}; % B7
        \node [Assembly, fill=\lowenr{coredata[A7_hyper]}] at ($( 7*\latWidth,1*\latWidth)$) {{{coredata[A7_content]}}}; % A7

        \node [Assembly, fill=\highenr{coredata[R8_hyper]}] at ($(-7*\latWidth,0*\latWidth)$) {{{coredata[R8_content]}}}; % R8
        \node [Assembly, fill=\noenr{coredata[P8_hyper]}] at ($(-6*\latWidth,0*\latWidth)$) {{{coredata[P8_content]}}}; % P8
        \node [Assembly, fill=\noenr{coredata[N8_hyper]}] at ($(-5*\latWidth,0*\latWidth)$) {{{coredata[N8_content]}}}; % N8
        \node [Assembly, fill=\noenr{coredata[M8_hyper]}] at ($(-4*\latWidth,0*\latWidth)$) {{{coredata[M8_content]}}}; % M8
        \node [Assembly, fill=\noenr{coredata[L8_hyper]}] at ($(-3*\latWidth,0*\latWidth)$) {{{coredata[L8_content]}}}; % L8
        \node [Assembly, fill=\noenr{coredata[K8_hyper]}] at ($(-2*\latWidth,0*\latWidth)$) {{{coredata[K8_content]}}}; % K8
        \node [Assembly, fill=\noenr{coredata[J8_hyper]}] at ($(-1*\latWidth,0*\latWidth)$) {{{coredata[J8_content]}}}; % J8
        \node [Assembly, fill=\noenr{coredata[H8_hyper]}] at ($(-0*\latWidth,0*\latWidth)$) {{{coredata[H8_content]}}}; % H8
        \node [Assembly, fill=\noenr{coredata[G8_hyper]}] at ($( 1*\latWidth,0*\latWidth)$) {{{coredata[G8_content]}}}; % G8
        \node [Assembly, fill=\noenr{coredata[F8_hyper]}] at ($( 2*\latWidth,0*\latWidth)$) {{{coredata[F8_content]}}}; % F8
        \node [Assembly, fill=\noenr{coredata[E8_hyper]}] at ($( 3*\latWidth,0*\latWidth)$) {{{coredata[E8_content]}}}; % E8
        \node [Assembly, fill=\noenr{coredata[D8_hyper]}] at ($( 4*\latWidth,0*\latWidth)$) {{{coredata[D8_content]}}}; % D8
        \node [Assembly, fill=\noenr{coredata[C8_hyper]}] at ($( 5*\latWidth,0*\latWidth)$) {{{coredata[C8_content]}}}; % C8
        \node [Assembly, fill=\noenr{coredata[B8_hyper]}] at ($( 6*\latWidth,0*\latWidth)$) {{{coredata[B8_content]}}}; % B8
        \node [Assembly, fill=\highenr{coredata[A8_hyper]}] at ($( 7*\latWidth,0*\latWidth)$) {{{coredata[A8_content]}}}; % A8

        \node [Assembly, fill=\lowenr{coredata[R9_hyper]}] at ($(-7*\latWidth,-1*\latWidth)$) {{{coredata[R9_content]}}}; % R9
        \node [Assembly, fill=\noenr{coredata[P9_hyper]}] at ($(-6*\latWidth,-1*\latWidth)$) {{{coredata[P9_content]}}}; % P9
        \node [Assembly, fill=\noenr{coredata[N9_hyper]}] at ($(-5*\latWidth,-1*\latWidth)$) {{{coredata[N9_content]}}}; % N9
        \node [Assembly, fill=\noenr{coredata[M9_hyper]}] at ($(-4*\latWidth,-1*\latWidth)$) {{{coredata[M9_content]}}}; % M9
        \node [Assembly, fill=\noenr{coredata[L9_hyper]}] at ($(-3*\latWidth,-1*\latWidth)$) {{{coredata[L9_content]}}}; % L9
        \node [Assembly, fill=\noenr{coredata[K9_hyper]}] at ($(-2*\latWidth,-1*\latWidth)$) {{{coredata[K9_content]}}}; % K9
        \node [Assembly, fill=\noenr{coredata[J9_hyper]}] at ($(-1*\latWidth,-1*\latWidth)$) {{{coredata[J9_content]}}}; % J9
        \node [Assembly, fill=\noenr{coredata[H9_hyper]}] at ($(-0*\latWidth,-1*\latWidth)$) {{{coredata[H9_content]}}}; % H9
        \node [Assembly, fill=\noenr{coredata[G9_hyper]}] at ($( 1*\latWidth,-1*\latWidth)$) {{{coredata[G9_content]}}}; % G9
        \node [Assembly, fill=\noenr{coredata[F9_hyper]}] at ($( 2*\latWidth,-1*\latWidth)$) {{{coredata[F9_content]}}}; % F9
        \node [Assembly, fill=\noenr{coredata[E9_hyper]}] at ($( 3*\latWidth,-1*\latWidth)$) {{{coredata[E9_content]}}}; % E9
        \node [Assembly, fill=\noenr{coredata[D9_hyper]}] at ($( 4*\latWidth,-1*\latWidth)$) {{{coredata[D9_content]}}}; % D9
        \node [Assembly, fill=\noenr{coredata[C9_hyper]}] at ($( 5*\latWidth,-1*\latWidth)$) {{{coredata[C9_content]}}}; % C9
        \node [Assembly, fill=\noenr{coredata[B9_hyper]}] at ($( 6*\latWidth,-1*\latWidth)$) {{{coredata[B9_content]}}}; % B9
        \node [Assembly, fill=\lowenr{coredata[A9_hyper]}] at ($( 7*\latWidth,-1*\latWidth)$) {{{coredata[A9_content]}}}; % A9

        \node [Assembly, fill=\highenr{coredata[R10_hyper]}] at ($(-7*\latWidth,-2*\latWidth)$) {{{coredata[R10_content]}}}; % R10
        \node [Assembly, fill=\noenr{coredata[P10_hyper]}] at ($(-6*\latWidth,-2*\latWidth)$) {{{coredata[P10_content]}}}; % P10
        \node [Assembly, fill=\lowenr{coredata[N10_hyper]}] at ($(-5*\latWidth,-2*\latWidth)$) {{{coredata[N10_content]}}}; % N10
        \node [Assembly, fill=\noenr{coredata[M10_hyper]}] at ($(-4*\latWidth,-2*\latWidth)$) {{{coredata[M10_content]}}}; % M10
        \node [Assembly, fill=\lowenr{coredata[L10_hyper]}] at ($(-3*\latWidth,-2*\latWidth)$) {{{coredata[L10_content]}}}; % L10
        \node [Assembly, fill=\noenr{coredata[K10_hyper]}] at ($(-2*\latWidth,-2*\latWidth)$) {{{coredata[K10_content]}}}; % K10
        \node [Assembly, fill=\noenr{coredata[J10_hyper]}] at ($(-1*\latWidth,-2*\latWidth)$) {{{coredata[J10_content]}}}; % J10
        \node [Assembly, fill=\noenr{coredata[H10_hyper]}] at ($(-0*\latWidth,-2*\latWidth)$) {{{coredata[H10_content]}}}; % H10
        \node [Assembly, fill=\noenr{coredata[G10_hyper]}] at ($( 1*\latWidth,-2*\latWidth)$) {{{coredata[G10_content]}}}; % G10
        \node [Assembly, fill=\noenr{coredata[F10_hyper]}] at ($( 2*\latWidth,-2*\latWidth)$) {{{coredata[F10_content]}}}; % F10
        \node [Assembly, fill=\lowenr{coredata[E10_hyper]}] at ($( 3*\latWidth,-2*\latWidth)$) {{{coredata[E10_content]}}}; % E10
        \node [Assembly, fill=\noenr{coredata[D10_hyper]}] at ($( 4*\latWidth,-2*\latWidth)$) {{{coredata[D10_content]}}}; % D10
        \node [Assembly, fill=\lowenr{coredata[C10_hyper]}] at ($( 5*\latWidth,-2*\latWidth)$) {{{coredata[C10_content]}}}; % C10
        \node [Assembly, fill=\noenr{coredata[B10_hyper]}] at ($( 6*\latWidth,-2*\latWidth)$) {{{coredata[B10_content]}}}; % B10
        \node [Assembly, fill=\highenr{coredata[A10_hyper]}] at ($( 7*\latWidth,-2*\latWidth)$) {{{coredata[A10_content]}}}; % A10

        \node [Assembly, fill=\noenr{coredata[R11_hyper]}] at ($(-7*\latWidth,-3*\latWidth)$) {{{coredata[R11_content]}}}; % R11
        \node [Assembly, fill=\lowenr{coredata[P11_hyper]}] at ($(-6*\latWidth,-3*\latWidth)$) {{{coredata[P11_content]}}}; % P11
        \node [Assembly, fill=\noenr{coredata[N11_hyper]}] at ($(-5*\latWidth,-3*\latWidth)$) {{{coredata[N11_content]}}}; % N11
        \node [Assembly, fill=\lowenr{coredata[M11_hyper]}] at ($(-4*\latWidth,-3*\latWidth)$) {{{coredata[M11_content]}}}; % M11
        \node [Assembly, fill=\noenr{coredata[L11_hyper]}] at ($(-3*\latWidth,-3*\latWidth)$) {{{coredata[L11_content]}}}; % L11
        \node [Assembly, fill=\lowenr{coredata[K11_hyper]}] at ($(-2*\latWidth,-3*\latWidth)$) {{{coredata[K11_content]}}}; % K11
        \node [Assembly, fill=\noenr{coredata[J11_hyper]}] at ($(-1*\latWidth,-3*\latWidth)$) {{{coredata[J11_content]}}}; % J11
        \node [Assembly, fill=\noenr{coredata[H11_hyper]}] at ($(-0*\latWidth,-3*\latWidth)$) {{{coredata[H11_content]}}}; % H11
        \node [Assembly, fill=\noenr{coredata[G11_hyper]}] at ($( 1*\latWidth,-3*\latWidth)$) {{{coredata[G11_content]}}}; % G11
        \node [Assembly, fill=\lowenr{coredata[F11_hyper]}] at ($( 2*\latWidth,-3*\latWidth)$) {{{coredata[F11_content]}}}; % F11
        \node [Assembly, fill=\noenr{coredata[E11_hyper]}] at ($( 3*\latWidth,-3*\latWidth)$) {{{coredata[E11_content]}}}; % E11
        \node [Assembly, fill=\lowenr{coredata[D11_hyper]}] at ($( 4*\latWidth,-3*\latWidth)$) {{{coredata[D11_content]}}}; % D11
        \node [Assembly, fill=\noenr{coredata[C11_hyper]}] at ($( 5*\latWidth,-3*\latWidth)$) {{{coredata[C11_content]}}}; % C11
        \node [Assembly, fill=\lowenr{coredata[B11_hyper]}] at ($( 6*\latWidth,-3*\latWidth)$) {{{coredata[B11_content]}}}; % B11
        \node [Assembly, fill=\noenr{coredata[A11_hyper]}] at ($( 7*\latWidth,-3*\latWidth)$) {{{coredata[A11_content]}}}; % A11

        \node [Assembly, fill=\lowenr{coredata[P12_hyper]}] at ($(-6*\latWidth,-4*\latWidth)$) {{{coredata[P12_content]}}}; % P12
        \node [Assembly, fill=\noenr{coredata[N12_hyper]}] at ($(-5*\latWidth,-4*\latWidth)$) {{{coredata[N12_content]}}}; % N12
        \node [Assembly, fill=\noenr{coredata[M12_hyper]}] at ($(-4*\latWidth,-4*\latWidth)$) {{{coredata[M12_content]}}}; % M12
        \node [Assembly, fill=\lowenr{coredata[L12_hyper]}] at ($(-3*\latWidth,-4*\latWidth)$) {{{coredata[L12_content]}}}; % L12
        \node [Assembly, fill=\noenr{coredata[K12_hyper]}] at ($(-2*\latWidth,-4*\latWidth)$) {{{coredata[K12_content]}}}; % K12
        \node [Assembly, fill=\noenr{coredata[J12_hyper]}] at ($(-1*\latWidth,-4*\latWidth)$) {{{coredata[J12_content]}}}; % J12
        \node [Assembly, fill=\noenr{coredata[H12_hyper]}] at ($(-0*\latWidth,-4*\latWidth)$) {{{coredata[H12_content]}}}; % H12
        \node [Assembly, fill=\noenr{coredata[G12_hyper]}] at ($( 1*\latWidth,-4*\latWidth)$) {{{coredata[G12_content]}}}; % G12
        \node [Assembly, fill=\noenr{coredata[F12_hyper]}] at ($( 2*\latWidth,-4*\latWidth)$) {{{coredata[F12_content]}}}; % F12
        \node [Assembly, fill=\lowenr{coredata[E12_hyper]}] at ($( 3*\latWidth,-4*\latWidth)$) {{{coredata[E12_content]}}}; % E12
        \node [Assembly, fill=\noenr{coredata[D12_hyper]}] at ($( 4*\latWidth,-4*\latWidth)$) {{{coredata[D12_content]}}}; % D12
        \node [Assembly, fill=\noenr{coredata[C12_hyper]}] at ($( 5*\latWidth,-4*\latWidth)$) {{{coredata[C12_content]}}}; % C12
        \node [Assembly, fill=\lowenr{coredata[B12_hyper]}] at ($( 6*\latWidth,-4*\latWidth)$) {{{coredata[B12_content]}}}; % B12

        \node [Assembly, fill=\noenr{coredata[P13_hyper]}] at ($(-6*\latWidth,-5*\latWidth)$) {{{coredata[P13_content]}}}; % P13
        \node [Assembly, fill=\highenr{coredata[N13_hyper]}] at ($(-5*\latWidth,-5*\latWidth)$) {{{coredata[N13_content]}}}; % N13
        \node [Assembly, fill=\noenr{coredata[M13_hyper]}] at ($(-4*\latWidth,-5*\latWidth)$) {{{coredata[M13_content]}}}; % M13
        \node [Assembly, fill=\noenr{coredata[L13_hyper]}] at ($(-3*\latWidth,-5*\latWidth)$) {{{coredata[L13_content]}}}; % L13
        \node [Assembly, fill=\lowenr{coredata[K13_hyper]}] at ($(-2*\latWidth,-5*\latWidth)$) {{{coredata[K13_content]}}}; % K13
        \node [Assembly, fill=\noenr{coredata[J13_hyper]}] at ($(-1*\latWidth,-5*\latWidth)$) {{{coredata[J13_content]}}}; % J13
        \node [Assembly, fill=\noenr{coredata[H13_hyper]}] at ($(-0*\latWidth,-5*\latWidth)$) {{{coredata[H13_content]}}}; % H13
        \node [Assembly, fill=\noenr{coredata[G13_hyper]}] at ($( 1*\latWidth,-5*\latWidth)$) {{{coredata[G13_content]}}}; % G13
        \node [Assembly, fill=\lowenr{coredata[F13_hyper]}] at ($( 2*\latWidth,-5*\latWidth)$) {{{coredata[F13_content]}}}; % F13
        \node [Assembly, fill=\noenr{coredata[E13_hyper]}] at ($( 3*\latWidth,-5*\latWidth)$) {{{coredata[E13_content]}}}; % E13
        \node [Assembly, fill=\noenr{coredata[D13_hyper]}] at ($( 4*\latWidth,-5*\latWidth)$) {{{coredata[D13_content]}}}; % D13
        \node [Assembly, fill=\highenr{coredata[C13_hyper]}] at ($( 5*\latWidth,-5*\latWidth)$) {{{coredata[C13_content]}}}; % C13
        \node [Assembly, fill=\noenr{coredata[B13_hyper]}] at ($( 6*\latWidth,-5*\latWidth)$) {{{coredata[B13_content]}}}; % B13

        \node [Assembly, fill=\noenr{coredata[N14_hyper]}] at ($(-5*\latWidth,-6*\latWidth)$) {{{coredata[N14_content]}}}; % N14
        \node [Assembly, fill=\lowenr{coredata[M14_hyper]}] at ($(-4*\latWidth,-6*\latWidth)$) {{{coredata[M14_content]}}}; % M14
        \node [Assembly, fill=\lowenr{coredata[L14_hyper]}] at ($(-3*\latWidth,-6*\latWidth)$) {{{coredata[L14_content]}}}; % L14
        \node [Assembly, fill=\noenr{coredata[K14_hyper]}] at ($(-2*\latWidth,-6*\latWidth)$) {{{coredata[K14_content]}}}; % K14
        \node [Assembly, fill=\noenr{coredata[J14_hyper]}] at ($(-1*\latWidth,-6*\latWidth)$) {{{coredata[J14_content]}}}; % J14
        \node [Assembly, fill=\noenr{coredata[H14_hyper]}] at ($(-0*\latWidth,-6*\latWidth)$) {{{coredata[H14_content]}}}; % H14
        \node [Assembly, fill=\noenr{coredata[G14_hyper]}] at ($( 1*\latWidth,-6*\latWidth)$) {{{coredata[G14_content]}}}; % G14
        \node [Assembly, fill=\noenr{coredata[F14_hyper]}] at ($( 2*\latWidth,-6*\latWidth)$) {{{coredata[F14_content]}}}; % F14
        \node [Assembly, fill=\lowenr{coredata[E14_hyper]}] at ($( 3*\latWidth,-6*\latWidth)$) {{{coredata[E14_content]}}}; % E14
        \node [Assembly, fill=\lowenr{coredata[D14_hyper]}] at ($( 4*\latWidth,-6*\latWidth)$) {{{coredata[D14_content]}}}; % D14
        \node [Assembly, fill=\noenr{coredata[C14_hyper]}] at ($( 5*\latWidth,-6*\latWidth)$) {{{coredata[C14_content]}}}; % C14

        \node [Assembly, fill=\noenr{coredata[L15_hyper]}] at ($(-3*\latWidth,-7*\latWidth)$) {{{coredata[L15_content]}}}; % L15
        \node [Assembly, fill=\highenr{coredata[K15_hyper]}] at ($(-2*\latWidth,-7*\latWidth)$) {{{coredata[K15_content]}}}; % K15
        \node [Assembly, fill=\lowenr{coredata[J15_hyper]}] at ($(-1*\latWidth,-7*\latWidth)$) {{{coredata[J15_content]}}}; % J15
        \node [Assembly, fill=\highenr{coredata[H15_hyper]}] at ($(-0*\latWidth,-7*\latWidth)$) {{{coredata[H15_content]}}}; % H15
        \node [Assembly, fill=\lowenr{coredata[G15_hyper]}] at ($( 1*\latWidth,-7*\latWidth)$) {{{coredata[G15_content]}}}; % G15
        \node [Assembly, fill=\highenr{coredata[F15_hyper]}] at ($( 2*\latWidth,-7*\latWidth)$) {{{coredata[F15_content]}}}; % F15
        \node [Assembly, fill=\noenr{coredata[E15_hyper]}] at ($( 3*\latWidth,-7*\latWidth)$) {{{coredata[E15_content]}}}; % E15

      \end{{tikzpicture}}
    }}

{legend}

    \caption{altcap}{{{caption} \label{{{label}}}}}
\end{{figure}}

"""

quart_fig_t_c2 = r"""
\begin{{figure}}[htbp]
    \centering

    % these dimensions are determined in arrow_dimms.ods

    \def\scale{{{scale}}}

    \def\latWidth{{0.2673473684*\scale}}

    \def\RPVOR{{3*\scale}}
    \def\rectW{{0.75*\scale}}
    \def\RPVIR{{2.7315789474*\scale}}
    \def\BarrelIR{{2.3368421053*\scale}}
    \def\BarrelOR{{2.4078947368*\scale}}
    \def\ShieldIR{{2.4223787816*\scale}}
    \def\ShieldOR{{2.5067965189*\scale}}
    \def\LinerIR{{2.7246166598*\scale}}

    \def\bafCIRx{{0.9357157895*\scale}}
    \def\bafCIRy{{2.0051052632*\scale}}
    \def\bafCORx{{0.9633473684*\scale}}
    \def\bafCORy{{2.0327368421*\scale}}
    \def\bafMIRx{{1.7377578947*\scale}}
    \def\bafMIRy{{1.4704105263*\scale}}
    \def\bafMORx{{1.7653894737*\scale}}
    \def\bafMORy{{1.4980421053*\scale}}

    \tikzset{{Assembly/.style={{
        inner sep=0pt,
        text width=\latWidth in,
        minimum size=\latWidth in,
        draw=black,
        align=center
        }}
    }}

    \def\tkzRPV{{(0,0) circle (\RPVIR) (0,0) circle (\RPVOR)}}
    \def\tkzLiner{{(0,0) circle (\LinerIR) (0,0) circle (\RPVIR)}}
    \def\tkzBarrel{{(0,0) circle (\BarrelIR) (0,0) circle (\BarrelOR)}}
    \def\tkzShields{{(0,0) circle (\ShieldIR) (0,0) circle (\ShieldOR)}}

    \def\tkzBaffCOR{{(-\bafCORx, -\bafCORy) rectangle (\bafCORx, \bafCORy)}}
    \def\tkzBaffCIR{{(-\bafCIRx, -\bafCIRy) rectangle (\bafCIRx, \bafCIRy)}}
    \def\tkzBaffMOR{{(-\bafMORx, -\bafMORy) rectangle (\bafMORx, \bafMORy)}}
    \def\tkzBaffMIR{{(-\bafMIRx, -\bafMIRy) rectangle (\bafMIRx, \bafMIRy) }}
    \def\tkzBaffleC{{ \tkzBaffCIR \tkzBaffCOR }}
    \def\tkzBaffleM{{ \tkzBaffMIR \tkzBaffMOR }}

    \def\tkzBaffCClip{{\tkzBaffCIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}
    \def\tkzBaffMClip{{\tkzBaffMIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}

    \def\noenr{{black!10}}
    \def\lowenr{{green!50}}
    \def\highenr{{orange!50}}

    \scalebox{{{scalebox}}}{{

      \begin{{tikzpicture}}[x=1in,y=1in]

        {struct}\begin{{scope}}
          {struct}\clip ($(-\latWidth/2,\latWidth/2)$) rectangle (\RPVOR,-\RPVOR);
          % draw RPV, barrel, and shield panels

          {struct}\path[fill=black!90!white,even odd rule] \tkzRPV;
          {struct}\path[fill=black,even odd rule] \tkzLiner;
          {struct}\path[fill=black,even odd rule] \tkzBarrel;
          {struct}\begin{{scope}}
          {struct}  \clip (0,0) -- +(61:\RPVOR) arc (61:29:\RPVOR) --
          {struct}        (0,0) -- +(151:\RPVOR) arc (151:119:\RPVOR) --
          {struct}        (0,0) -- +(241:\RPVOR) arc (241:209:\RPVOR) --
          {struct}        (0,0) -- +(331:\RPVOR) arc (331:299:\RPVOR) -- cycle;
          {struct}  \path[fill=black,even odd rule] \tkzShields;
          {struct}\end{{scope}}

          % draw baffle north/south

          {struct}\begin{{scope}}[even odd rule]
          {struct}  \clip[rotate=90] \tkzBaffMClip;
          {struct}  \path[fill=black] \tkzBaffleC;
          {struct}\end{{scope}}
          {struct}\begin{{scope}}[even odd rule]
          {struct}  \clip \tkzBaffCClip;
          {struct}  \clip \tkzBaffMClip;
          {struct}  \path[fill=black, rotate=90] \tkzBaffleM;
          {struct}\end{{scope}}

          % draw baffle east/west

          {struct}\begin{{scope}}[rotate=90]
          {struct}  \begin{{scope}}[even odd rule]
          {struct}    \clip[rotate=90] \tkzBaffMClip;
          {struct}    \path[fill=black] \tkzBaffleC;
          {struct}  \end{{scope}}
          {struct}  \begin{{scope}}[even odd rule]
          {struct}    \clip \tkzBaffCClip;
          {struct}    \clip \tkzBaffMClip;
          {struct}    \path[fill=black, rotate=90] \tkzBaffleM;
          {struct}  \end{{scope}}
          {struct}\end{{scope}}

        {struct}\end{{scope}}

        % draw assembly row/column headers

        \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{H}} -- ($(-0*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{G}} -- ($(1*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{F}} -- ($(2*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{E}} -- ($(3*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{D}} -- ($(4*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{C}} -- ($(5*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{B}} -- ($(6*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{A}} -- ($(7*\latWidth,{head_llm}*\latWidth)$);

        \begin{{scope}}[rotate=90]
          \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{15}} -- ($(-7*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{14}} -- ($(-6*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{13}} -- ($(-5*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{12}} -- ($(-4*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{11}} -- ($(-3*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{10}} -- ($(-2*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{9}} -- ($(-1*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{8}} -- ($(-0*\latWidth,{head_llm}*\latWidth)$);
        \end{{scope}}

        % draw fuel assembly nodes

        \node [Assembly, fill=\noenr{coredata[H8_hyper]}] at ($(-0*\latWidth,0*\latWidth)$) {{{coredata[H8_content]}}}; % H8
        \node [Assembly, fill=\noenr{coredata[G8_hyper]}] at ($( 1*\latWidth,0*\latWidth)$) {{{coredata[G8_content]}}}; % G8
        \node [Assembly, fill=\noenr{coredata[F8_hyper]}] at ($( 2*\latWidth,0*\latWidth)$) {{{coredata[F8_content]}}}; % F8
        \node [Assembly, fill=\noenr{coredata[E8_hyper]}] at ($( 3*\latWidth,0*\latWidth)$) {{{coredata[E8_content]}}}; % E8
        \node [Assembly, fill=\noenr{coredata[D8_hyper]}] at ($( 4*\latWidth,0*\latWidth)$) {{{coredata[D8_content]}}}; % D8
        \node [Assembly, fill=\noenr{coredata[C8_hyper]}] at ($( 5*\latWidth,0*\latWidth)$) {{{coredata[C8_content]}}}; % C8
        \node [Assembly, fill=\noenr{coredata[B8_hyper]}] at ($( 6*\latWidth,0*\latWidth)$) {{{coredata[B8_content]}}}; % B8
        \node [Assembly, fill=\highenr{coredata[A8_hyper]}] at ($( 7*\latWidth,0*\latWidth)$) {{{coredata[A8_content]}}}; % A8

        \node [Assembly, fill=\noenr{coredata[H9_hyper]}] at ($(-0*\latWidth,-1*\latWidth)$) {{{coredata[H9_content]}}}; % H9
        \node [Assembly, fill=\noenr{coredata[G9_hyper]}] at ($( 1*\latWidth,-1*\latWidth)$) {{{coredata[G9_content]}}}; % G9
        \node [Assembly, fill=\noenr{coredata[F9_hyper]}] at ($( 2*\latWidth,-1*\latWidth)$) {{{coredata[F9_content]}}}; % F9
        \node [Assembly, fill=\noenr{coredata[E9_hyper]}] at ($( 3*\latWidth,-1*\latWidth)$) {{{coredata[E9_content]}}}; % E9
        \node [Assembly, fill=\noenr{coredata[D9_hyper]}] at ($( 4*\latWidth,-1*\latWidth)$) {{{coredata[D9_content]}}}; % D9
        \node [Assembly, fill=\noenr{coredata[C9_hyper]}] at ($( 5*\latWidth,-1*\latWidth)$) {{{coredata[C9_content]}}}; % C9
        \node [Assembly, fill=\noenr{coredata[B9_hyper]}] at ($( 6*\latWidth,-1*\latWidth)$) {{{coredata[B9_content]}}}; % B9
        \node [Assembly, fill=\lowenr{coredata[A9_hyper]}] at ($( 7*\latWidth,-1*\latWidth)$) {{{coredata[A9_content]}}}; % A9

        \node [Assembly, fill=\noenr{coredata[H10_hyper]}] at ($(-0*\latWidth,-2*\latWidth)$) {{{coredata[H10_content]}}}; % H10
        \node [Assembly, fill=\noenr{coredata[G10_hyper]}] at ($( 1*\latWidth,-2*\latWidth)$) {{{coredata[G10_content]}}}; % G10
        \node [Assembly, fill=\noenr{coredata[F10_hyper]}] at ($( 2*\latWidth,-2*\latWidth)$) {{{coredata[F10_content]}}}; % F10
        \node [Assembly, fill=\lowenr{coredata[E10_hyper]}] at ($( 3*\latWidth,-2*\latWidth)$) {{{coredata[E10_content]}}}; % E10
        \node [Assembly, fill=\noenr{coredata[D10_hyper]}] at ($( 4*\latWidth,-2*\latWidth)$) {{{coredata[D10_content]}}}; % D10
        \node [Assembly, fill=\lowenr{coredata[C10_hyper]}] at ($( 5*\latWidth,-2*\latWidth)$) {{{coredata[C10_content]}}}; % C10
        \node [Assembly, fill=\noenr{coredata[B10_hyper]}] at ($( 6*\latWidth,-2*\latWidth)$) {{{coredata[B10_content]}}}; % B10
        \node [Assembly, fill=\highenr{coredata[A10_hyper]}] at ($( 7*\latWidth,-2*\latWidth)$) {{{coredata[A10_content]}}}; % A10

        \node [Assembly, fill=\noenr{coredata[H11_hyper]}] at ($(-0*\latWidth,-3*\latWidth)$) {{{coredata[H11_content]}}}; % H11
        \node [Assembly, fill=\noenr{coredata[G11_hyper]}] at ($( 1*\latWidth,-3*\latWidth)$) {{{coredata[G11_content]}}}; % G11
        \node [Assembly, fill=\lowenr{coredata[F11_hyper]}] at ($( 2*\latWidth,-3*\latWidth)$) {{{coredata[F11_content]}}}; % F11
        \node [Assembly, fill=\noenr{coredata[E11_hyper]}] at ($( 3*\latWidth,-3*\latWidth)$) {{{coredata[E11_content]}}}; % E11
        \node [Assembly, fill=\lowenr{coredata[D11_hyper]}] at ($( 4*\latWidth,-3*\latWidth)$) {{{coredata[D11_content]}}}; % D11
        \node [Assembly, fill=\noenr{coredata[C11_hyper]}] at ($( 5*\latWidth,-3*\latWidth)$) {{{coredata[C11_content]}}}; % C11
        \node [Assembly, fill=\lowenr{coredata[B11_hyper]}] at ($( 6*\latWidth,-3*\latWidth)$) {{{coredata[B11_content]}}}; % B11
        \node [Assembly, fill=\noenr{coredata[A11_hyper]}] at ($( 7*\latWidth,-3*\latWidth)$) {{{coredata[A11_content]}}}; % A11

        \node [Assembly, fill=\noenr{coredata[H12_hyper]}] at ($(-0*\latWidth,-4*\latWidth)$) {{{coredata[H12_content]}}}; % H12
        \node [Assembly, fill=\noenr{coredata[G12_hyper]}] at ($( 1*\latWidth,-4*\latWidth)$) {{{coredata[G12_content]}}}; % G12
        \node [Assembly, fill=\noenr{coredata[F12_hyper]}] at ($( 2*\latWidth,-4*\latWidth)$) {{{coredata[F12_content]}}}; % F12
        \node [Assembly, fill=\lowenr{coredata[E12_hyper]}] at ($( 3*\latWidth,-4*\latWidth)$) {{{coredata[E12_content]}}}; % E12
        \node [Assembly, fill=\noenr{coredata[D12_hyper]}] at ($( 4*\latWidth,-4*\latWidth)$) {{{coredata[D12_content]}}}; % D12
        \node [Assembly, fill=\noenr{coredata[C12_hyper]}] at ($( 5*\latWidth,-4*\latWidth)$) {{{coredata[C12_content]}}}; % C12
        \node [Assembly, fill=\lowenr{coredata[B12_hyper]}] at ($( 6*\latWidth,-4*\latWidth)$) {{{coredata[B12_content]}}}; % B12

        \node [Assembly, fill=\noenr{coredata[H13_hyper]}] at ($(-0*\latWidth,-5*\latWidth)$) {{{coredata[H13_content]}}}; % H13
        \node [Assembly, fill=\noenr{coredata[G13_hyper]}] at ($( 1*\latWidth,-5*\latWidth)$) {{{coredata[G13_content]}}}; % G13
        \node [Assembly, fill=\lowenr{coredata[F13_hyper]}] at ($( 2*\latWidth,-5*\latWidth)$) {{{coredata[F13_content]}}}; % F13
        \node [Assembly, fill=\noenr{coredata[E13_hyper]}] at ($( 3*\latWidth,-5*\latWidth)$) {{{coredata[E13_content]}}}; % E13
        \node [Assembly, fill=\noenr{coredata[D13_hyper]}] at ($( 4*\latWidth,-5*\latWidth)$) {{{coredata[D13_content]}}}; % D13
        \node [Assembly, fill=\highenr{coredata[C13_hyper]}] at ($( 5*\latWidth,-5*\latWidth)$) {{{coredata[C13_content]}}}; % C13
        \node [Assembly, fill=\noenr{coredata[B13_hyper]}] at ($( 6*\latWidth,-5*\latWidth)$) {{{coredata[B13_content]}}}; % B13

        \node [Assembly, fill=\noenr{coredata[H14_hyper]}] at ($(-0*\latWidth,-6*\latWidth)$) {{{coredata[H14_content]}}}; % H14
        \node [Assembly, fill=\noenr{coredata[G14_hyper]}] at ($( 1*\latWidth,-6*\latWidth)$) {{{coredata[G14_content]}}}; % G14
        \node [Assembly, fill=\noenr{coredata[F14_hyper]}] at ($( 2*\latWidth,-6*\latWidth)$) {{{coredata[F14_content]}}}; % F14
        \node [Assembly, fill=\lowenr{coredata[E14_hyper]}] at ($( 3*\latWidth,-6*\latWidth)$) {{{coredata[E14_content]}}}; % E14
        \node [Assembly, fill=\lowenr{coredata[D14_hyper]}] at ($( 4*\latWidth,-6*\latWidth)$) {{{coredata[D14_content]}}}; % D14
        \node [Assembly, fill=\noenr{coredata[C14_hyper]}] at ($( 5*\latWidth,-6*\latWidth)$) {{{coredata[C14_content]}}}; % C14

        \node [Assembly, fill=\highenr{coredata[H15_hyper]}] at ($(-0*\latWidth,-7*\latWidth)$) {{{coredata[H15_content]}}}; % H15
        \node [Assembly, fill=\lowenr{coredata[G15_hyper]}] at ($( 1*\latWidth,-7*\latWidth)$) {{{coredata[G15_content]}}}; % G15
        \node [Assembly, fill=\highenr{coredata[F15_hyper]}] at ($( 2*\latWidth,-7*\latWidth)$) {{{coredata[F15_content]}}}; % F15
        \node [Assembly, fill=\noenr{coredata[E15_hyper]}] at ($( 3*\latWidth,-7*\latWidth)$) {{{coredata[E15_content]}}}; % E15
      \end{{tikzpicture}}
    }}

{legend}

    \caption{altcap}{{{caption} \label{{{label}}}}}
\end{{figure}}

"""


main_fig_clr_t = r"""
\begin{{figure}}[htbp]
    \centering

    % these dimensions are determined in arrow_dimms.ods

    \def\scale{{{scale}}}

    \def\latWidth{{0.2673473684*\scale}}

    \def\RPVOR{{3*\scale}}
    \def\rectW{{0.75*\scale}}
    \def\RPVIR{{2.7315789474*\scale}}
    \def\BarrelIR{{2.3368421053*\scale}}
    \def\BarrelOR{{2.4078947368*\scale}}
    \def\ShieldIR{{2.4223787816*\scale}}
    \def\ShieldOR{{2.5067965189*\scale}}
    \def\LinerIR{{2.7246166598*\scale}}

    \def\bafCIRx{{0.9357157895*\scale}}
    \def\bafCIRy{{2.0051052632*\scale}}
    \def\bafCORx{{0.9633473684*\scale}}
    \def\bafCORy{{2.0327368421*\scale}}
    \def\bafMIRx{{1.7377578947*\scale}}
    \def\bafMIRy{{1.4704105263*\scale}}
    \def\bafMORx{{1.7653894737*\scale}}
    \def\bafMORy{{1.4980421053*\scale}}

    \tikzset{{Assembly/.style={{
        inner sep=0pt,
        text width=\latWidth in,
        minimum size=\latWidth in,
        draw=black,
        align=center
        }}
    }}

    \def\tkzRPV{{(0,0) circle (\RPVIR) (0,0) circle (\RPVOR)}}
    \def\tkzLiner{{(0,0) circle (\LinerIR) (0,0) circle (\RPVIR)}}
    \def\tkzBarrel{{(0,0) circle (\BarrelIR) (0,0) circle (\BarrelOR)}}
    \def\tkzShields{{(0,0) circle (\ShieldIR) (0,0) circle (\ShieldOR)}}

    \def\tkzBaffCOR{{(-\bafCORx, -\bafCORy) rectangle (\bafCORx, \bafCORy)}}
    \def\tkzBaffCIR{{(-\bafCIRx, -\bafCIRy) rectangle (\bafCIRx, \bafCIRy)}}
    \def\tkzBaffMOR{{(-\bafMORx, -\bafMORy) rectangle (\bafMORx, \bafMORy)}}
    \def\tkzBaffMIR{{(-\bafMIRx, -\bafMIRy) rectangle (\bafMIRx, \bafMIRy) }}
    \def\tkzBaffleC{{ \tkzBaffCIR \tkzBaffCOR }}
    \def\tkzBaffleM{{ \tkzBaffMIR \tkzBaffMOR }}

    \def\tkzBaffCClip{{\tkzBaffCIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}
    \def\tkzBaffMClip{{\tkzBaffMIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}

    \def\highenr{{blue!50}}
    \def\midenr{{yellow!50}}
    \def\lowenr{{red!50}}

    \scalebox{{{scalebox}}}{{

      \begin{{tikzpicture}}[x=1in,y=1in]

        % draw RPV, barrel, and shield panels

        {struct}\path[fill=black!90!white,even odd rule] \tkzRPV;
        {struct}\path[fill=black,even odd rule] \tkzLiner;
        {struct}\path[fill=black,even odd rule] \tkzBarrel;
        {struct}\begin{{scope}}
        {struct}  \clip (0,0) -- +(61:\RPVOR) arc (61:29:\RPVOR) --
        {struct}        (0,0) -- +(151:\RPVOR) arc (151:119:\RPVOR) --
        {struct}        (0,0) -- +(241:\RPVOR) arc (241:209:\RPVOR) --
        {struct}        (0,0) -- +(331:\RPVOR) arc (331:299:\RPVOR) -- cycle;
        {struct}  \path[fill=black,even odd rule] \tkzShields;
        {struct}\end{{scope}}

        % draw baffle north/south

        {struct}\begin{{scope}}[even odd rule]
        {struct}  \clip[rotate=90] \tkzBaffMClip;
        {struct}  \path[fill=black] \tkzBaffleC;
        {struct}\end{{scope}}
        {struct}\begin{{scope}}[even odd rule]
        {struct}  \clip \tkzBaffCClip;
        {struct}  \clip \tkzBaffMClip;
        {struct}  \path[fill=black, rotate=90] \tkzBaffleM;
        {struct}\end{{scope}}

        % draw baffle east/west

        {struct}\begin{{scope}}[rotate=90]
        {struct}  \begin{{scope}}[even odd rule]
        {struct}    \clip[rotate=90] \tkzBaffMClip;
        {struct}    \path[fill=black] \tkzBaffleC;
        {struct}  \end{{scope}}
        {struct}  \begin{{scope}}[even odd rule]
        {struct}    \clip \tkzBaffCClip;
        {struct}    \clip \tkzBaffMClip;
        {struct}    \path[fill=black, rotate=90] \tkzBaffleM;
        {struct}  \end{{scope}}
        {struct}\end{{scope}}

        % draw assembly row/column headers

        \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{R}} -- ($(-7*\latWidth,4*\latWidth)$);
        \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{P}} -- ($(-6*\latWidth,6*\latWidth)$);
        \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{N}} -- ($(-5*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{M}} -- ($(-4*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{L}} -- ($(-3*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{K}} -- ($(-2*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{J}} -- ($(-1*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{H}} -- ($(-0*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{G}} -- ($(1*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{F}} -- ($(2*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{E}} -- ($(3*\latWidth,8*\latWidth)$);
        \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{D}} -- ($(4*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{C}} -- ($(5*\latWidth,7*\latWidth)$);
        \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{B}} -- ($(6*\latWidth,6*\latWidth)$);
        \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{A}} -- ($(7*\latWidth,4*\latWidth)$);

        \begin{{scope}}[rotate=90]
          \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{15}} -- ($(-7*\latWidth,4*\latWidth)$);
          \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{14}} -- ($(-6*\latWidth,6*\latWidth)$);
          \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{13}} -- ($(-5*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{12}} -- ($(-4*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{11}} -- ($(-3*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{10}} -- ($(-2*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{9}} -- ($(-1*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{8}} -- ($(-0*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{7}} -- ($(1*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{6}} -- ($(2*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{5}} -- ($(3*\latWidth,8*\latWidth)$);
          \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{4}} -- ($(4*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{3}} -- ($(5*\latWidth,7*\latWidth)$);
          \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{2}} -- ($(6*\latWidth,6*\latWidth)$);
          \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{1}} -- ($(7*\latWidth,4*\latWidth)$);
        \end{{scope}}


        % draw fuel assembly nodes

        \node [Assembly, fill=Lonecolor{coredata[L1_hyper]}] at ($(-3*\latWidth,7*\latWidth)$) {{{coredata[L1_content]}}}; % L1
        \node [Assembly, fill=Konecolor{coredata[K1_hyper]}] at ($(-2*\latWidth,7*\latWidth)$) {{{coredata[K1_content]}}}; % K1
        \node [Assembly, fill=Jonecolor{coredata[J1_hyper]}] at ($(-1*\latWidth,7*\latWidth)$) {{{coredata[J1_content]}}}; % J1
        \node [Assembly, fill=Honecolor{coredata[H1_hyper]}] at ($(-0*\latWidth,7*\latWidth)$) {{{coredata[H1_content]}}}; % H1
        \node [Assembly, fill=Gonecolor{coredata[G1_hyper]}] at ($( 1*\latWidth,7*\latWidth)$) {{{coredata[G1_content]}}}; % G1
        \node [Assembly, fill=Fonecolor{coredata[F1_hyper]}] at ($( 2*\latWidth,7*\latWidth)$) {{{coredata[F1_content]}}}; % F1
        \node [Assembly, fill=Eonecolor{coredata[E1_hyper]}] at ($( 3*\latWidth,7*\latWidth)$) {{{coredata[E1_content]}}}; % E1

        \node [Assembly, fill=Ntwocolor{coredata[N2_hyper]}] at ($(-5*\latWidth,6*\latWidth)$) {{{coredata[N2_content]}}}; % N2
        \node [Assembly, fill=Mtwocolor{coredata[M2_hyper]}] at ($(-4*\latWidth,6*\latWidth)$) {{{coredata[M2_content]}}}; % M2
        \node [Assembly, fill=Ltwocolor{coredata[L2_hyper]}] at ($(-3*\latWidth,6*\latWidth)$) {{{coredata[L2_content]}}}; % L2
        \node [Assembly, fill=Ktwocolor{coredata[K2_hyper]}] at ($(-2*\latWidth,6*\latWidth)$) {{{coredata[K2_content]}}}; % K2
        \node [Assembly, fill=Jtwocolor{coredata[J2_hyper]}] at ($(-1*\latWidth,6*\latWidth)$) {{{coredata[J2_content]}}}; % J2
        \node [Assembly, fill=Htwocolor{coredata[H2_hyper]}] at ($(-0*\latWidth,6*\latWidth)$) {{{coredata[H2_content]}}}; % H2
        \node [Assembly, fill=Gtwocolor{coredata[G2_hyper]}] at ($( 1*\latWidth,6*\latWidth)$) {{{coredata[G2_content]}}}; % G2
        \node [Assembly, fill=Ftwocolor{coredata[F2_hyper]}] at ($( 2*\latWidth,6*\latWidth)$) {{{coredata[F2_content]}}}; % F2
        \node [Assembly, fill=Etwocolor{coredata[E2_hyper]}] at ($( 3*\latWidth,6*\latWidth)$) {{{coredata[E2_content]}}}; % E2
        \node [Assembly, fill=Dtwocolor{coredata[D2_hyper]}] at ($( 4*\latWidth,6*\latWidth)$) {{{coredata[D2_content]}}}; % D2
        \node [Assembly, fill=Ctwocolor{coredata[C2_hyper]}] at ($( 5*\latWidth,6*\latWidth)$) {{{coredata[C2_content]}}}; % C2

        \node [Assembly, fill=Pthreecolor{coredata[P3_hyper]}] at ($(-6*\latWidth,5*\latWidth)$) {{{coredata[P3_content]}}}; % P3
        \node [Assembly, fill=Nthreecolor{coredata[N3_hyper]}] at ($(-5*\latWidth,5*\latWidth)$) {{{coredata[N3_content]}}}; % N3
        \node [Assembly, fill=Mthreecolor{coredata[M3_hyper]}] at ($(-4*\latWidth,5*\latWidth)$) {{{coredata[M3_content]}}}; % M3
        \node [Assembly, fill=Lthreecolor{coredata[L3_hyper]}] at ($(-3*\latWidth,5*\latWidth)$) {{{coredata[L3_content]}}}; % L3
        \node [Assembly, fill=Kthreecolor{coredata[K3_hyper]}] at ($(-2*\latWidth,5*\latWidth)$) {{{coredata[K3_content]}}}; % K3
        \node [Assembly, fill=Jthreecolor{coredata[J3_hyper]}] at ($(-1*\latWidth,5*\latWidth)$) {{{coredata[J3_content]}}}; % J3
        \node [Assembly, fill=Hthreecolor{coredata[H3_hyper]}] at ($(-0*\latWidth,5*\latWidth)$) {{{coredata[H3_content]}}}; % H3
        \node [Assembly, fill=Gthreecolor{coredata[G3_hyper]}] at ($( 1*\latWidth,5*\latWidth)$) {{{coredata[G3_content]}}}; % G3
        \node [Assembly, fill=Fthreecolor{coredata[F3_hyper]}] at ($( 2*\latWidth,5*\latWidth)$) {{{coredata[F3_content]}}}; % F3
        \node [Assembly, fill=Ethreecolor{coredata[E3_hyper]}] at ($( 3*\latWidth,5*\latWidth)$) {{{coredata[E3_content]}}}; % E3
        \node [Assembly, fill=Dthreecolor{coredata[D3_hyper]}] at ($( 4*\latWidth,5*\latWidth)$) {{{coredata[D3_content]}}}; % D3
        \node [Assembly, fill=Cthreecolor{coredata[C3_hyper]}] at ($( 5*\latWidth,5*\latWidth)$) {{{coredata[C3_content]}}}; % C3
        \node [Assembly, fill=Bthreecolor{coredata[B3_hyper]}] at ($( 6*\latWidth,5*\latWidth)$) {{{coredata[B3_content]}}}; % B3

        \node [Assembly, fill=Pfourcolor{coredata[P4_hyper]}] at ($(-6*\latWidth,4*\latWidth)$) {{{coredata[P4_content]}}}; % P4
        \node [Assembly, fill=Nfourcolor{coredata[N4_hyper]}] at ($(-5*\latWidth,4*\latWidth)$) {{{coredata[N4_content]}}}; % N4
        \node [Assembly, fill=Mfourcolor{coredata[M4_hyper]}] at ($(-4*\latWidth,4*\latWidth)$) {{{coredata[M4_content]}}}; % M4
        \node [Assembly, fill=Lfourcolor{coredata[L4_hyper]}] at ($(-3*\latWidth,4*\latWidth)$) {{{coredata[L4_content]}}}; % L4
        \node [Assembly, fill=Kfourcolor{coredata[K4_hyper]}] at ($(-2*\latWidth,4*\latWidth)$) {{{coredata[K4_content]}}}; % K4
        \node [Assembly, fill=Jfourcolor{coredata[J4_hyper]}] at ($(-1*\latWidth,4*\latWidth)$) {{{coredata[J4_content]}}}; % J4
        \node [Assembly, fill=Hfourcolor{coredata[H4_hyper]}] at ($(-0*\latWidth,4*\latWidth)$) {{{coredata[H4_content]}}}; % H4
        \node [Assembly, fill=Gfourcolor{coredata[G4_hyper]}] at ($( 1*\latWidth,4*\latWidth)$) {{{coredata[G4_content]}}}; % G4
        \node [Assembly, fill=Ffourcolor{coredata[F4_hyper]}] at ($( 2*\latWidth,4*\latWidth)$) {{{coredata[F4_content]}}}; % F4
        \node [Assembly, fill=Efourcolor{coredata[E4_hyper]}] at ($( 3*\latWidth,4*\latWidth)$) {{{coredata[E4_content]}}}; % E4
        \node [Assembly, fill=Dfourcolor{coredata[D4_hyper]}] at ($( 4*\latWidth,4*\latWidth)$) {{{coredata[D4_content]}}}; % D4
        \node [Assembly, fill=Cfourcolor{coredata[C4_hyper]}] at ($( 5*\latWidth,4*\latWidth)$) {{{coredata[C4_content]}}}; % C4
        \node [Assembly, fill=Bfourcolor{coredata[B4_hyper]}] at ($( 6*\latWidth,4*\latWidth)$) {{{coredata[B4_content]}}}; % B4

        \node [Assembly, fill=Rfivecolor{coredata[R5_hyper]}] at ($(-7*\latWidth,3*\latWidth)$) {{{coredata[R5_content]}}}; % R5
        \node [Assembly, fill=Pfivecolor{coredata[P5_hyper]}] at ($(-6*\latWidth,3*\latWidth)$) {{{coredata[P5_content]}}}; % P5
        \node [Assembly, fill=Nfivecolor{coredata[N5_hyper]}] at ($(-5*\latWidth,3*\latWidth)$) {{{coredata[N5_content]}}}; % N5
        \node [Assembly, fill=Mfivecolor{coredata[M5_hyper]}] at ($(-4*\latWidth,3*\latWidth)$) {{{coredata[M5_content]}}}; % M5
        \node [Assembly, fill=Lfivecolor{coredata[L5_hyper]}] at ($(-3*\latWidth,3*\latWidth)$) {{{coredata[L5_content]}}}; % L5
        \node [Assembly, fill=Kfivecolor{coredata[K5_hyper]}] at ($(-2*\latWidth,3*\latWidth)$) {{{coredata[K5_content]}}}; % K5
        \node [Assembly, fill=Jfivecolor{coredata[J5_hyper]}] at ($(-1*\latWidth,3*\latWidth)$) {{{coredata[J5_content]}}}; % J5
        \node [Assembly, fill=Hfivecolor{coredata[H5_hyper]}] at ($(-0*\latWidth,3*\latWidth)$) {{{coredata[H5_content]}}}; % H5
        \node [Assembly, fill=Gfivecolor{coredata[G5_hyper]}] at ($( 1*\latWidth,3*\latWidth)$) {{{coredata[G5_content]}}}; % G5
        \node [Assembly, fill=Ffivecolor{coredata[F5_hyper]}] at ($( 2*\latWidth,3*\latWidth)$) {{{coredata[F5_content]}}}; % F5
        \node [Assembly, fill=Efivecolor{coredata[E5_hyper]}] at ($( 3*\latWidth,3*\latWidth)$) {{{coredata[E5_content]}}}; % E5
        \node [Assembly, fill=Dfivecolor{coredata[D5_hyper]}] at ($( 4*\latWidth,3*\latWidth)$) {{{coredata[D5_content]}}}; % D5
        \node [Assembly, fill=Cfivecolor{coredata[C5_hyper]}] at ($( 5*\latWidth,3*\latWidth)$) {{{coredata[C5_content]}}}; % C5
        \node [Assembly, fill=Bfivecolor{coredata[B5_hyper]}] at ($( 6*\latWidth,3*\latWidth)$) {{{coredata[B5_content]}}}; % B5
        \node [Assembly, fill=Afivecolor{coredata[A5_hyper]}] at ($( 7*\latWidth,3*\latWidth)$) {{{coredata[A5_content]}}}; % A5

        \node [Assembly, fill=Rsixcolor{coredata[R6_hyper]}] at ($(-7*\latWidth,2*\latWidth)$) {{{coredata[R6_content]}}}; % R6
        \node [Assembly, fill=Psixcolor{coredata[P6_hyper]}] at ($(-6*\latWidth,2*\latWidth)$) {{{coredata[P6_content]}}}; % P6
        \node [Assembly, fill=Nsixcolor{coredata[N6_hyper]}] at ($(-5*\latWidth,2*\latWidth)$) {{{coredata[N6_content]}}}; % N6
        \node [Assembly, fill=Msixcolor{coredata[M6_hyper]}] at ($(-4*\latWidth,2*\latWidth)$) {{{coredata[M6_content]}}}; % M6
        \node [Assembly, fill=Lsixcolor{coredata[L6_hyper]}] at ($(-3*\latWidth,2*\latWidth)$) {{{coredata[L6_content]}}}; % L6
        \node [Assembly, fill=Ksixcolor{coredata[K6_hyper]}] at ($(-2*\latWidth,2*\latWidth)$) {{{coredata[K6_content]}}}; % K6
        \node [Assembly, fill=Jsixcolor{coredata[J6_hyper]}] at ($(-1*\latWidth,2*\latWidth)$) {{{coredata[J6_content]}}}; % J6
        \node [Assembly, fill=Hsixcolor{coredata[H6_hyper]}] at ($(-0*\latWidth,2*\latWidth)$) {{{coredata[H6_content]}}}; % H6
        \node [Assembly, fill=Gsixcolor{coredata[G6_hyper]}] at ($( 1*\latWidth,2*\latWidth)$) {{{coredata[G6_content]}}}; % G6
        \node [Assembly, fill=Fsixcolor{coredata[F6_hyper]}] at ($( 2*\latWidth,2*\latWidth)$) {{{coredata[F6_content]}}}; % F6
        \node [Assembly, fill=Esixcolor{coredata[E6_hyper]}] at ($( 3*\latWidth,2*\latWidth)$) {{{coredata[E6_content]}}}; % E6
        \node [Assembly, fill=Dsixcolor{coredata[D6_hyper]}] at ($( 4*\latWidth,2*\latWidth)$) {{{coredata[D6_content]}}}; % D6
        \node [Assembly, fill=Csixcolor{coredata[C6_hyper]}] at ($( 5*\latWidth,2*\latWidth)$) {{{coredata[C6_content]}}}; % C6
        \node [Assembly, fill=Bsixcolor{coredata[B6_hyper]}] at ($( 6*\latWidth,2*\latWidth)$) {{{coredata[B6_content]}}}; % B6
        \node [Assembly, fill=Asixcolor{coredata[A6_hyper]}] at ($( 7*\latWidth,2*\latWidth)$) {{{coredata[A6_content]}}}; % A6

        \node [Assembly, fill=Rsevencolor{coredata[R7_hyper]}] at ($(-7*\latWidth,1*\latWidth)$) {{{coredata[R7_content]}}}; % R7
        \node [Assembly, fill=Psevencolor{coredata[P7_hyper]}] at ($(-6*\latWidth,1*\latWidth)$) {{{coredata[P7_content]}}}; % P7
        \node [Assembly, fill=Nsevencolor{coredata[N7_hyper]}] at ($(-5*\latWidth,1*\latWidth)$) {{{coredata[N7_content]}}}; % N7
        \node [Assembly, fill=Msevencolor{coredata[M7_hyper]}] at ($(-4*\latWidth,1*\latWidth)$) {{{coredata[M7_content]}}}; % M7
        \node [Assembly, fill=Lsevencolor{coredata[L7_hyper]}] at ($(-3*\latWidth,1*\latWidth)$) {{{coredata[L7_content]}}}; % L7
        \node [Assembly, fill=Ksevencolor{coredata[K7_hyper]}] at ($(-2*\latWidth,1*\latWidth)$) {{{coredata[K7_content]}}}; % K7
        \node [Assembly, fill=Jsevencolor{coredata[J7_hyper]}] at ($(-1*\latWidth,1*\latWidth)$) {{{coredata[J7_content]}}}; % J7
        \node [Assembly, fill=Hsevencolor{coredata[H7_hyper]}] at ($(-0*\latWidth,1*\latWidth)$) {{{coredata[H7_content]}}}; % H7
        \node [Assembly, fill=Gsevencolor{coredata[G7_hyper]}] at ($( 1*\latWidth,1*\latWidth)$) {{{coredata[G7_content]}}}; % G7
        \node [Assembly, fill=Fsevencolor{coredata[F7_hyper]}] at ($( 2*\latWidth,1*\latWidth)$) {{{coredata[F7_content]}}}; % F7
        \node [Assembly, fill=Esevencolor{coredata[E7_hyper]}] at ($( 3*\latWidth,1*\latWidth)$) {{{coredata[E7_content]}}}; % E7
        \node [Assembly, fill=Dsevencolor{coredata[D7_hyper]}] at ($( 4*\latWidth,1*\latWidth)$) {{{coredata[D7_content]}}}; % D7
        \node [Assembly, fill=Csevencolor{coredata[C7_hyper]}] at ($( 5*\latWidth,1*\latWidth)$) {{{coredata[C7_content]}}}; % C7
        \node [Assembly, fill=Bsevencolor{coredata[B7_hyper]}] at ($( 6*\latWidth,1*\latWidth)$) {{{coredata[B7_content]}}}; % B7
        \node [Assembly, fill=Asevencolor{coredata[A7_hyper]}] at ($( 7*\latWidth,1*\latWidth)$) {{{coredata[A7_content]}}}; % A7

        \node [Assembly, fill=Reightcolor{coredata[R8_hyper]}] at ($(-7*\latWidth,0*\latWidth)$) {{{coredata[R8_content]}}}; % R8
        \node [Assembly, fill=Peightcolor{coredata[P8_hyper]}] at ($(-6*\latWidth,0*\latWidth)$) {{{coredata[P8_content]}}}; % P8
        \node [Assembly, fill=Neightcolor{coredata[N8_hyper]}] at ($(-5*\latWidth,0*\latWidth)$) {{{coredata[N8_content]}}}; % N8
        \node [Assembly, fill=Meightcolor{coredata[M8_hyper]}] at ($(-4*\latWidth,0*\latWidth)$) {{{coredata[M8_content]}}}; % M8
        \node [Assembly, fill=Leightcolor{coredata[L8_hyper]}] at ($(-3*\latWidth,0*\latWidth)$) {{{coredata[L8_content]}}}; % L8
        \node [Assembly, fill=Keightcolor{coredata[K8_hyper]}] at ($(-2*\latWidth,0*\latWidth)$) {{{coredata[K8_content]}}}; % K8
        \node [Assembly, fill=Jeightcolor{coredata[J8_hyper]}] at ($(-1*\latWidth,0*\latWidth)$) {{{coredata[J8_content]}}}; % J8
        \node [Assembly, fill=Heightcolor{coredata[H8_hyper]}] at ($(-0*\latWidth,0*\latWidth)$) {{{coredata[H8_content]}}}; % H8
        \node [Assembly, fill=Geightcolor{coredata[G8_hyper]}] at ($( 1*\latWidth,0*\latWidth)$) {{{coredata[G8_content]}}}; % G8
        \node [Assembly, fill=Feightcolor{coredata[F8_hyper]}] at ($( 2*\latWidth,0*\latWidth)$) {{{coredata[F8_content]}}}; % F8
        \node [Assembly, fill=Eeightcolor{coredata[E8_hyper]}] at ($( 3*\latWidth,0*\latWidth)$) {{{coredata[E8_content]}}}; % E8
        \node [Assembly, fill=Deightcolor{coredata[D8_hyper]}] at ($( 4*\latWidth,0*\latWidth)$) {{{coredata[D8_content]}}}; % D8
        \node [Assembly, fill=Ceightcolor{coredata[C8_hyper]}] at ($( 5*\latWidth,0*\latWidth)$) {{{coredata[C8_content]}}}; % C8
        \node [Assembly, fill=Beightcolor{coredata[B8_hyper]}] at ($( 6*\latWidth,0*\latWidth)$) {{{coredata[B8_content]}}}; % B8
        \node [Assembly, fill=Aeightcolor{coredata[A8_hyper]}] at ($( 7*\latWidth,0*\latWidth)$) {{{coredata[A8_content]}}}; % A8

        \node [Assembly, fill=Rninecolor{coredata[R9_hyper]}] at ($(-7*\latWidth,-1*\latWidth)$) {{{coredata[R9_content]}}}; % R9
        \node [Assembly, fill=Pninecolor{coredata[P9_hyper]}] at ($(-6*\latWidth,-1*\latWidth)$) {{{coredata[P9_content]}}}; % P9
        \node [Assembly, fill=Nninecolor{coredata[N9_hyper]}] at ($(-5*\latWidth,-1*\latWidth)$) {{{coredata[N9_content]}}}; % N9
        \node [Assembly, fill=Mninecolor{coredata[M9_hyper]}] at ($(-4*\latWidth,-1*\latWidth)$) {{{coredata[M9_content]}}}; % M9
        \node [Assembly, fill=Lninecolor{coredata[L9_hyper]}] at ($(-3*\latWidth,-1*\latWidth)$) {{{coredata[L9_content]}}}; % L9
        \node [Assembly, fill=Kninecolor{coredata[K9_hyper]}] at ($(-2*\latWidth,-1*\latWidth)$) {{{coredata[K9_content]}}}; % K9
        \node [Assembly, fill=Jninecolor{coredata[J9_hyper]}] at ($(-1*\latWidth,-1*\latWidth)$) {{{coredata[J9_content]}}}; % J9
        \node [Assembly, fill=Hninecolor{coredata[H9_hyper]}] at ($(-0*\latWidth,-1*\latWidth)$) {{{coredata[H9_content]}}}; % H9
        \node [Assembly, fill=Gninecolor{coredata[G9_hyper]}] at ($( 1*\latWidth,-1*\latWidth)$) {{{coredata[G9_content]}}}; % G9
        \node [Assembly, fill=Fninecolor{coredata[F9_hyper]}] at ($( 2*\latWidth,-1*\latWidth)$) {{{coredata[F9_content]}}}; % F9
        \node [Assembly, fill=Eninecolor{coredata[E9_hyper]}] at ($( 3*\latWidth,-1*\latWidth)$) {{{coredata[E9_content]}}}; % E9
        \node [Assembly, fill=Dninecolor{coredata[D9_hyper]}] at ($( 4*\latWidth,-1*\latWidth)$) {{{coredata[D9_content]}}}; % D9
        \node [Assembly, fill=Cninecolor{coredata[C9_hyper]}] at ($( 5*\latWidth,-1*\latWidth)$) {{{coredata[C9_content]}}}; % C9
        \node [Assembly, fill=Bninecolor{coredata[B9_hyper]}] at ($( 6*\latWidth,-1*\latWidth)$) {{{coredata[B9_content]}}}; % B9
        \node [Assembly, fill=Aninecolor{coredata[A9_hyper]}] at ($( 7*\latWidth,-1*\latWidth)$) {{{coredata[A9_content]}}}; % A9

        \node [Assembly, fill=Rtencolor{coredata[R10_hyper]}] at ($(-7*\latWidth,-2*\latWidth)$) {{{coredata[R10_content]}}}; % R10
        \node [Assembly, fill=Ptencolor{coredata[P10_hyper]}] at ($(-6*\latWidth,-2*\latWidth)$) {{{coredata[P10_content]}}}; % P10
        \node [Assembly, fill=Ntencolor{coredata[N10_hyper]}] at ($(-5*\latWidth,-2*\latWidth)$) {{{coredata[N10_content]}}}; % N10
        \node [Assembly, fill=Mtencolor{coredata[M10_hyper]}] at ($(-4*\latWidth,-2*\latWidth)$) {{{coredata[M10_content]}}}; % M10
        \node [Assembly, fill=Ltencolor{coredata[L10_hyper]}] at ($(-3*\latWidth,-2*\latWidth)$) {{{coredata[L10_content]}}}; % L10
        \node [Assembly, fill=Ktencolor{coredata[K10_hyper]}] at ($(-2*\latWidth,-2*\latWidth)$) {{{coredata[K10_content]}}}; % K10
        \node [Assembly, fill=Jtencolor{coredata[J10_hyper]}] at ($(-1*\latWidth,-2*\latWidth)$) {{{coredata[J10_content]}}}; % J10
        \node [Assembly, fill=Htencolor{coredata[H10_hyper]}] at ($(-0*\latWidth,-2*\latWidth)$) {{{coredata[H10_content]}}}; % H10
        \node [Assembly, fill=Gtencolor{coredata[G10_hyper]}] at ($( 1*\latWidth,-2*\latWidth)$) {{{coredata[G10_content]}}}; % G10
        \node [Assembly, fill=Ftencolor{coredata[F10_hyper]}] at ($( 2*\latWidth,-2*\latWidth)$) {{{coredata[F10_content]}}}; % F10
        \node [Assembly, fill=Etencolor{coredata[E10_hyper]}] at ($( 3*\latWidth,-2*\latWidth)$) {{{coredata[E10_content]}}}; % E10
        \node [Assembly, fill=Dtencolor{coredata[D10_hyper]}] at ($( 4*\latWidth,-2*\latWidth)$) {{{coredata[D10_content]}}}; % D10
        \node [Assembly, fill=Ctencolor{coredata[C10_hyper]}] at ($( 5*\latWidth,-2*\latWidth)$) {{{coredata[C10_content]}}}; % C10
        \node [Assembly, fill=Btencolor{coredata[B10_hyper]}] at ($( 6*\latWidth,-2*\latWidth)$) {{{coredata[B10_content]}}}; % B10
        \node [Assembly, fill=Atencolor{coredata[A10_hyper]}] at ($( 7*\latWidth,-2*\latWidth)$) {{{coredata[A10_content]}}}; % A10

        \node [Assembly, fill=Relevencolor{coredata[R11_hyper]}] at ($(-7*\latWidth,-3*\latWidth)$) {{{coredata[R11_content]}}}; % R11
        \node [Assembly, fill=Pelevencolor{coredata[P11_hyper]}] at ($(-6*\latWidth,-3*\latWidth)$) {{{coredata[P11_content]}}}; % P11
        \node [Assembly, fill=Nelevencolor{coredata[N11_hyper]}] at ($(-5*\latWidth,-3*\latWidth)$) {{{coredata[N11_content]}}}; % N11
        \node [Assembly, fill=Melevencolor{coredata[M11_hyper]}] at ($(-4*\latWidth,-3*\latWidth)$) {{{coredata[M11_content]}}}; % M11
        \node [Assembly, fill=Lelevencolor{coredata[L11_hyper]}] at ($(-3*\latWidth,-3*\latWidth)$) {{{coredata[L11_content]}}}; % L11
        \node [Assembly, fill=Kelevencolor{coredata[K11_hyper]}] at ($(-2*\latWidth,-3*\latWidth)$) {{{coredata[K11_content]}}}; % K11
        \node [Assembly, fill=Jelevencolor{coredata[J11_hyper]}] at ($(-1*\latWidth,-3*\latWidth)$) {{{coredata[J11_content]}}}; % J11
        \node [Assembly, fill=Helevencolor{coredata[H11_hyper]}] at ($(-0*\latWidth,-3*\latWidth)$) {{{coredata[H11_content]}}}; % H11
        \node [Assembly, fill=Gelevencolor{coredata[G11_hyper]}] at ($( 1*\latWidth,-3*\latWidth)$) {{{coredata[G11_content]}}}; % G11
        \node [Assembly, fill=Felevencolor{coredata[F11_hyper]}] at ($( 2*\latWidth,-3*\latWidth)$) {{{coredata[F11_content]}}}; % F11
        \node [Assembly, fill=Eelevencolor{coredata[E11_hyper]}] at ($( 3*\latWidth,-3*\latWidth)$) {{{coredata[E11_content]}}}; % E11
        \node [Assembly, fill=Delevencolor{coredata[D11_hyper]}] at ($( 4*\latWidth,-3*\latWidth)$) {{{coredata[D11_content]}}}; % D11
        \node [Assembly, fill=Celevencolor{coredata[C11_hyper]}] at ($( 5*\latWidth,-3*\latWidth)$) {{{coredata[C11_content]}}}; % C11
        \node [Assembly, fill=Belevencolor{coredata[B11_hyper]}] at ($( 6*\latWidth,-3*\latWidth)$) {{{coredata[B11_content]}}}; % B11
        \node [Assembly, fill=Aelevencolor{coredata[A11_hyper]}] at ($( 7*\latWidth,-3*\latWidth)$) {{{coredata[A11_content]}}}; % A11

        \node [Assembly, fill=Ptwelvecolor{coredata[P12_hyper]}] at ($(-6*\latWidth,-4*\latWidth)$) {{{coredata[P12_content]}}}; % P12
        \node [Assembly, fill=Ntwelvecolor{coredata[N12_hyper]}] at ($(-5*\latWidth,-4*\latWidth)$) {{{coredata[N12_content]}}}; % N12
        \node [Assembly, fill=Mtwelvecolor{coredata[M12_hyper]}] at ($(-4*\latWidth,-4*\latWidth)$) {{{coredata[M12_content]}}}; % M12
        \node [Assembly, fill=Ltwelvecolor{coredata[L12_hyper]}] at ($(-3*\latWidth,-4*\latWidth)$) {{{coredata[L12_content]}}}; % L12
        \node [Assembly, fill=Ktwelvecolor{coredata[K12_hyper]}] at ($(-2*\latWidth,-4*\latWidth)$) {{{coredata[K12_content]}}}; % K12
        \node [Assembly, fill=Jtwelvecolor{coredata[J12_hyper]}] at ($(-1*\latWidth,-4*\latWidth)$) {{{coredata[J12_content]}}}; % J12
        \node [Assembly, fill=Htwelvecolor{coredata[H12_hyper]}] at ($(-0*\latWidth,-4*\latWidth)$) {{{coredata[H12_content]}}}; % H12
        \node [Assembly, fill=Gtwelvecolor{coredata[G12_hyper]}] at ($( 1*\latWidth,-4*\latWidth)$) {{{coredata[G12_content]}}}; % G12
        \node [Assembly, fill=Ftwelvecolor{coredata[F12_hyper]}] at ($( 2*\latWidth,-4*\latWidth)$) {{{coredata[F12_content]}}}; % F12
        \node [Assembly, fill=Etwelvecolor{coredata[E12_hyper]}] at ($( 3*\latWidth,-4*\latWidth)$) {{{coredata[E12_content]}}}; % E12
        \node [Assembly, fill=Dtwelvecolor{coredata[D12_hyper]}] at ($( 4*\latWidth,-4*\latWidth)$) {{{coredata[D12_content]}}}; % D12
        \node [Assembly, fill=Ctwelvecolor{coredata[C12_hyper]}] at ($( 5*\latWidth,-4*\latWidth)$) {{{coredata[C12_content]}}}; % C12
        \node [Assembly, fill=Btwelvecolor{coredata[B12_hyper]}] at ($( 6*\latWidth,-4*\latWidth)$) {{{coredata[B12_content]}}}; % B12

        \node [Assembly, fill=Pthirteencolor{coredata[P13_hyper]}] at ($(-6*\latWidth,-5*\latWidth)$) {{{coredata[P13_content]}}}; % P13
        \node [Assembly, fill=Nthirteencolor{coredata[N13_hyper]}] at ($(-5*\latWidth,-5*\latWidth)$) {{{coredata[N13_content]}}}; % N13
        \node [Assembly, fill=Mthirteencolor{coredata[M13_hyper]}] at ($(-4*\latWidth,-5*\latWidth)$) {{{coredata[M13_content]}}}; % M13
        \node [Assembly, fill=Lthirteencolor{coredata[L13_hyper]}] at ($(-3*\latWidth,-5*\latWidth)$) {{{coredata[L13_content]}}}; % L13
        \node [Assembly, fill=Kthirteencolor{coredata[K13_hyper]}] at ($(-2*\latWidth,-5*\latWidth)$) {{{coredata[K13_content]}}}; % K13
        \node [Assembly, fill=Jthirteencolor{coredata[J13_hyper]}] at ($(-1*\latWidth,-5*\latWidth)$) {{{coredata[J13_content]}}}; % J13
        \node [Assembly, fill=Hthirteencolor{coredata[H13_hyper]}] at ($(-0*\latWidth,-5*\latWidth)$) {{{coredata[H13_content]}}}; % H13
        \node [Assembly, fill=Gthirteencolor{coredata[G13_hyper]}] at ($( 1*\latWidth,-5*\latWidth)$) {{{coredata[G13_content]}}}; % G13
        \node [Assembly, fill=Fthirteencolor{coredata[F13_hyper]}] at ($( 2*\latWidth,-5*\latWidth)$) {{{coredata[F13_content]}}}; % F13
        \node [Assembly, fill=Ethirteencolor{coredata[E13_hyper]}] at ($( 3*\latWidth,-5*\latWidth)$) {{{coredata[E13_content]}}}; % E13
        \node [Assembly, fill=Dthirteencolor{coredata[D13_hyper]}] at ($( 4*\latWidth,-5*\latWidth)$) {{{coredata[D13_content]}}}; % D13
        \node [Assembly, fill=Cthirteencolor{coredata[C13_hyper]}] at ($( 5*\latWidth,-5*\latWidth)$) {{{coredata[C13_content]}}}; % C13
        \node [Assembly, fill=Bthirteencolor{coredata[B13_hyper]}] at ($( 6*\latWidth,-5*\latWidth)$) {{{coredata[B13_content]}}}; % B13

        \node [Assembly, fill=Nfourteencolor{coredata[N14_hyper]}] at ($(-5*\latWidth,-6*\latWidth)$) {{{coredata[N14_content]}}}; % N14
        \node [Assembly, fill=Mfourteencolor{coredata[M14_hyper]}] at ($(-4*\latWidth,-6*\latWidth)$) {{{coredata[M14_content]}}}; % M14
        \node [Assembly, fill=Lfourteencolor{coredata[L14_hyper]}] at ($(-3*\latWidth,-6*\latWidth)$) {{{coredata[L14_content]}}}; % L14
        \node [Assembly, fill=Kfourteencolor{coredata[K14_hyper]}] at ($(-2*\latWidth,-6*\latWidth)$) {{{coredata[K14_content]}}}; % K14
        \node [Assembly, fill=Jfourteencolor{coredata[J14_hyper]}] at ($(-1*\latWidth,-6*\latWidth)$) {{{coredata[J14_content]}}}; % J14
        \node [Assembly, fill=Hfourteencolor{coredata[H14_hyper]}] at ($(-0*\latWidth,-6*\latWidth)$) {{{coredata[H14_content]}}}; % H14
        \node [Assembly, fill=Gfourteencolor{coredata[G14_hyper]}] at ($( 1*\latWidth,-6*\latWidth)$) {{{coredata[G14_content]}}}; % G14
        \node [Assembly, fill=Ffourteencolor{coredata[F14_hyper]}] at ($( 2*\latWidth,-6*\latWidth)$) {{{coredata[F14_content]}}}; % F14
        \node [Assembly, fill=Efourteencolor{coredata[E14_hyper]}] at ($( 3*\latWidth,-6*\latWidth)$) {{{coredata[E14_content]}}}; % E14
        \node [Assembly, fill=Dfourteencolor{coredata[D14_hyper]}] at ($( 4*\latWidth,-6*\latWidth)$) {{{coredata[D14_content]}}}; % D14
        \node [Assembly, fill=Cfourteencolor{coredata[C14_hyper]}] at ($( 5*\latWidth,-6*\latWidth)$) {{{coredata[C14_content]}}}; % C14

        \node [Assembly, fill=Lfifteencolor{coredata[L15_hyper]}] at ($(-3*\latWidth,-7*\latWidth)$) {{{coredata[L15_content]}}}; % L15
        \node [Assembly, fill=Kfifteencolor{coredata[K15_hyper]}] at ($(-2*\latWidth,-7*\latWidth)$) {{{coredata[K15_content]}}}; % K15
        \node [Assembly, fill=Jfifteencolor{coredata[J15_hyper]}] at ($(-1*\latWidth,-7*\latWidth)$) {{{coredata[J15_content]}}}; % J15
        \node [Assembly, fill=Hfifteencolor{coredata[H15_hyper]}] at ($(-0*\latWidth,-7*\latWidth)$) {{{coredata[H15_content]}}}; % H15
        \node [Assembly, fill=Gfifteencolor{coredata[G15_hyper]}] at ($( 1*\latWidth,-7*\latWidth)$) {{{coredata[G15_content]}}}; % G15
        \node [Assembly, fill=Ffifteencolor{coredata[F15_hyper]}] at ($( 2*\latWidth,-7*\latWidth)$) {{{coredata[F15_content]}}}; % F15
        \node [Assembly, fill=Efifteencolor{coredata[E15_hyper]}] at ($( 3*\latWidth,-7*\latWidth)$) {{{coredata[E15_content]}}}; % E15

      \end{{tikzpicture}}
    }}

{legend}

    \caption{altcap}{{{caption} \label{{{label}}}}}
\end{{figure}}

"""


quart_fig_clr_t = r"""
\begin{{figure}}[htbp]
    \centering

    % these dimensions are determined in arrow_dimms.ods

    \def\scale{{{scale}}}

    \def\latWidth{{0.2673473684*\scale}}

    \def\RPVOR{{3*\scale}}
    \def\rectW{{0.75*\scale}}
    \def\RPVIR{{2.7315789474*\scale}}
    \def\BarrelIR{{2.3368421053*\scale}}
    \def\BarrelOR{{2.4078947368*\scale}}
    \def\ShieldIR{{2.4223787816*\scale}}
    \def\ShieldOR{{2.5067965189*\scale}}
    \def\LinerIR{{2.7246166598*\scale}}

    \def\bafCIRx{{0.9357157895*\scale}}
    \def\bafCIRy{{2.0051052632*\scale}}
    \def\bafCORx{{0.9633473684*\scale}}
    \def\bafCORy{{2.0327368421*\scale}}
    \def\bafMIRx{{1.7377578947*\scale}}
    \def\bafMIRy{{1.4704105263*\scale}}
    \def\bafMORx{{1.7653894737*\scale}}
    \def\bafMORy{{1.4980421053*\scale}}

    \tikzset{{Assembly/.style={{
        inner sep=0pt,
        text width=\latWidth in,
        minimum size=\latWidth in,
        draw=black,
        align=center
        }}
    }}

    \def\tkzRPV{{(0,0) circle (\RPVIR) (0,0) circle (\RPVOR)}}
    \def\tkzLiner{{(0,0) circle (\LinerIR) (0,0) circle (\RPVIR)}}
    \def\tkzBarrel{{(0,0) circle (\BarrelIR) (0,0) circle (\BarrelOR)}}
    \def\tkzShields{{(0,0) circle (\ShieldIR) (0,0) circle (\ShieldOR)}}

    \def\tkzBaffCOR{{(-\bafCORx, -\bafCORy) rectangle (\bafCORx, \bafCORy)}}
    \def\tkzBaffCIR{{(-\bafCIRx, -\bafCIRy) rectangle (\bafCIRx, \bafCIRy)}}
    \def\tkzBaffMOR{{(-\bafMORx, -\bafMORy) rectangle (\bafMORx, \bafMORy)}}
    \def\tkzBaffMIR{{(-\bafMIRx, -\bafMIRy) rectangle (\bafMIRx, \bafMIRy) }}
    \def\tkzBaffleC{{ \tkzBaffCIR \tkzBaffCOR }}
    \def\tkzBaffleM{{ \tkzBaffMIR \tkzBaffMOR }}

    \def\tkzBaffCClip{{\tkzBaffCIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}
    \def\tkzBaffMClip{{\tkzBaffMIR (-\RPVOR, -\RPVOR) rectangle (\RPVOR, \RPVOR)}}

    \def\highenr{{blue!50}}
    \def\midenr{{yellow!50}}
    \def\lowenr{{red!50}}

    \scalebox{{{scalebox}}}{{

      \begin{{tikzpicture}}[x=1in,y=1in]

        {struct}\begin{{scope}}
          {struct}\clip ($(-\latWidth/2,\latWidth/2)$) rectangle (\RPVOR,-\RPVOR);
          % draw RPV, barrel, and shield panels

          {struct}\path[fill=black!90!white,even odd rule] \tkzRPV;
          {struct}\path[fill=black,even odd rule] \tkzLiner;
          {struct}\path[fill=black,even odd rule] \tkzBarrel;
          {struct}\begin{{scope}}
          {struct}  \clip (0,0) -- +(61:\RPVOR) arc (61:29:\RPVOR) --
          {struct}        (0,0) -- +(151:\RPVOR) arc (151:119:\RPVOR) --
          {struct}        (0,0) -- +(241:\RPVOR) arc (241:209:\RPVOR) --
          {struct}        (0,0) -- +(331:\RPVOR) arc (331:299:\RPVOR) -- cycle;
          {struct}  \path[fill=black,even odd rule] \tkzShields;
          {struct}\end{{scope}}

          % draw baffle north/south

          {struct}\begin{{scope}}[even odd rule]
          {struct}  \clip[rotate=90] \tkzBaffMClip;
          {struct}  \path[fill=black] \tkzBaffleC;
          {struct}\end{{scope}}
          {struct}\begin{{scope}}[even odd rule]
          {struct}  \clip \tkzBaffCClip;
          {struct}  \clip \tkzBaffMClip;
          {struct}  \path[fill=black, rotate=90] \tkzBaffleM;
          {struct}\end{{scope}}

          % draw baffle east/west

          {struct}\begin{{scope}}[rotate=90]
          {struct}  \begin{{scope}}[even odd rule]
          {struct}    \clip[rotate=90] \tkzBaffMClip;
          {struct}    \path[fill=black] \tkzBaffleC;
          {struct}  \end{{scope}}
          {struct}  \begin{{scope}}[even odd rule]
          {struct}    \clip \tkzBaffCClip;
          {struct}    \clip \tkzBaffMClip;
          {struct}    \path[fill=black, rotate=90] \tkzBaffleM;
          {struct}  \end{{scope}}
          {struct}\end{{scope}}

        {struct}\end{{scope}}

        % draw assembly row/column headers

        \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{H}} -- ($(-0*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(1*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{G}} -- ($(1*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(2*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{F}} -- ($(2*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(3*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{E}} -- ($(3*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(4*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{D}} -- ($(4*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(5*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{C}} -- ($(5*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(6*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{B}} -- ($(6*\latWidth,{head_llm}*\latWidth)$);
        \draw[red, thick] ($(7*\latWidth,{head_lhm}*\latWidth)$) node[above, anchor=south] {{A}} -- ($(7*\latWidth,{head_llm}*\latWidth)$);

        \begin{{scope}}[rotate=90]
          \draw[red, thick] ($(-7*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{15}} -- ($(-7*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-6*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{14}} -- ($(-6*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-5*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{13}} -- ($(-5*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-4*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{12}} -- ($(-4*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-3*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{11}} -- ($(-3*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-2*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{10}} -- ($(-2*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-1*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{9}} -- ($(-1*\latWidth,{head_llm}*\latWidth)$);
          \draw[red, thick] ($(-0*\latWidth,{head_lhm}*\latWidth)$) node[left, anchor=east] {{8}} -- ($(-0*\latWidth,{head_llm}*\latWidth)$);
        \end{{scope}}

        % draw fuel assembly nodes

        \node [Assembly, fill=Heightcolor{coredata[H8_hyper]}] at ($(-0*\latWidth,0*\latWidth)$) {{{coredata[H8_content]}}}; % H8
        \node [Assembly, fill=Geightcolor{coredata[G8_hyper]}] at ($( 1*\latWidth,0*\latWidth)$) {{{coredata[G8_content]}}}; % G8
        \node [Assembly, fill=Feightcolor{coredata[F8_hyper]}] at ($( 2*\latWidth,0*\latWidth)$) {{{coredata[F8_content]}}}; % F8
        \node [Assembly, fill=Eeightcolor{coredata[E8_hyper]}] at ($( 3*\latWidth,0*\latWidth)$) {{{coredata[E8_content]}}}; % E8
        \node [Assembly, fill=Deightcolor{coredata[D8_hyper]}] at ($( 4*\latWidth,0*\latWidth)$) {{{coredata[D8_content]}}}; % D8
        \node [Assembly, fill=Ceightcolor{coredata[C8_hyper]}] at ($( 5*\latWidth,0*\latWidth)$) {{{coredata[C8_content]}}}; % C8
        \node [Assembly, fill=Beightcolor{coredata[B8_hyper]}] at ($( 6*\latWidth,0*\latWidth)$) {{{coredata[B8_content]}}}; % B8
        \node [Assembly, fill=Aeightcolor{coredata[A8_hyper]}] at ($( 7*\latWidth,0*\latWidth)$) {{{coredata[A8_content]}}}; % A8

        \node [Assembly, fill=Hninecolor{coredata[H9_hyper]}] at ($(-0*\latWidth,-1*\latWidth)$) {{{coredata[H9_content]}}}; % H9
        \node [Assembly, fill=Gninecolor{coredata[G9_hyper]}] at ($( 1*\latWidth,-1*\latWidth)$) {{{coredata[G9_content]}}}; % G9
        \node [Assembly, fill=Fninecolor{coredata[F9_hyper]}] at ($( 2*\latWidth,-1*\latWidth)$) {{{coredata[F9_content]}}}; % F9
        \node [Assembly, fill=Eninecolor{coredata[E9_hyper]}] at ($( 3*\latWidth,-1*\latWidth)$) {{{coredata[E9_content]}}}; % E9
        \node [Assembly, fill=Dninecolor{coredata[D9_hyper]}] at ($( 4*\latWidth,-1*\latWidth)$) {{{coredata[D9_content]}}}; % D9
        \node [Assembly, fill=Cninecolor{coredata[C9_hyper]}] at ($( 5*\latWidth,-1*\latWidth)$) {{{coredata[C9_content]}}}; % C9
        \node [Assembly, fill=Bninecolor{coredata[B9_hyper]}] at ($( 6*\latWidth,-1*\latWidth)$) {{{coredata[B9_content]}}}; % B9
        \node [Assembly, fill=Aninecolor{coredata[A9_hyper]}] at ($( 7*\latWidth,-1*\latWidth)$) {{{coredata[A9_content]}}}; % A9

        \node [Assembly, fill=Htencolor{coredata[H10_hyper]}] at ($(-0*\latWidth,-2*\latWidth)$) {{{coredata[H10_content]}}}; % H10
        \node [Assembly, fill=Gtencolor{coredata[G10_hyper]}] at ($( 1*\latWidth,-2*\latWidth)$) {{{coredata[G10_content]}}}; % G10
        \node [Assembly, fill=Ftencolor{coredata[F10_hyper]}] at ($( 2*\latWidth,-2*\latWidth)$) {{{coredata[F10_content]}}}; % F10
        \node [Assembly, fill=Etencolor{coredata[E10_hyper]}] at ($( 3*\latWidth,-2*\latWidth)$) {{{coredata[E10_content]}}}; % E10
        \node [Assembly, fill=Dtencolor{coredata[D10_hyper]}] at ($( 4*\latWidth,-2*\latWidth)$) {{{coredata[D10_content]}}}; % D10
        \node [Assembly, fill=Ctencolor{coredata[C10_hyper]}] at ($( 5*\latWidth,-2*\latWidth)$) {{{coredata[C10_content]}}}; % C10
        \node [Assembly, fill=Btencolor{coredata[B10_hyper]}] at ($( 6*\latWidth,-2*\latWidth)$) {{{coredata[B10_content]}}}; % B10
        \node [Assembly, fill=Atencolor{coredata[A10_hyper]}] at ($( 7*\latWidth,-2*\latWidth)$) {{{coredata[A10_content]}}}; % A10

        \node [Assembly, fill=Helevencolor{coredata[H11_hyper]}] at ($(-0*\latWidth,-3*\latWidth)$) {{{coredata[H11_content]}}}; % H11
        \node [Assembly, fill=Gelevencolor{coredata[G11_hyper]}] at ($( 1*\latWidth,-3*\latWidth)$) {{{coredata[G11_content]}}}; % G11
        \node [Assembly, fill=Felevencolor{coredata[F11_hyper]}] at ($( 2*\latWidth,-3*\latWidth)$) {{{coredata[F11_content]}}}; % F11
        \node [Assembly, fill=Eelevencolor{coredata[E11_hyper]}] at ($( 3*\latWidth,-3*\latWidth)$) {{{coredata[E11_content]}}}; % E11
        \node [Assembly, fill=Delevencolor{coredata[D11_hyper]}] at ($( 4*\latWidth,-3*\latWidth)$) {{{coredata[D11_content]}}}; % D11
        \node [Assembly, fill=Celevencolor{coredata[C11_hyper]}] at ($( 5*\latWidth,-3*\latWidth)$) {{{coredata[C11_content]}}}; % C11
        \node [Assembly, fill=Belevencolor{coredata[B11_hyper]}] at ($( 6*\latWidth,-3*\latWidth)$) {{{coredata[B11_content]}}}; % B11
        \node [Assembly, fill=Aelevencolor{coredata[A11_hyper]}] at ($( 7*\latWidth,-3*\latWidth)$) {{{coredata[A11_content]}}}; % A11

        \node [Assembly, fill=Htwelvecolor{coredata[H12_hyper]}] at ($(-0*\latWidth,-4*\latWidth)$) {{{coredata[H12_content]}}}; % H12
        \node [Assembly, fill=Gtwelvecolor{coredata[G12_hyper]}] at ($( 1*\latWidth,-4*\latWidth)$) {{{coredata[G12_content]}}}; % G12
        \node [Assembly, fill=Ftwelvecolor{coredata[F12_hyper]}] at ($( 2*\latWidth,-4*\latWidth)$) {{{coredata[F12_content]}}}; % F12
        \node [Assembly, fill=Etwelvecolor{coredata[E12_hyper]}] at ($( 3*\latWidth,-4*\latWidth)$) {{{coredata[E12_content]}}}; % E12
        \node [Assembly, fill=Dtwelvecolor{coredata[D12_hyper]}] at ($( 4*\latWidth,-4*\latWidth)$) {{{coredata[D12_content]}}}; % D12
        \node [Assembly, fill=Ctwelvecolor{coredata[C12_hyper]}] at ($( 5*\latWidth,-4*\latWidth)$) {{{coredata[C12_content]}}}; % C12
        \node [Assembly, fill=Btwelvecolor{coredata[B12_hyper]}] at ($( 6*\latWidth,-4*\latWidth)$) {{{coredata[B12_content]}}}; % B12

        \node [Assembly, fill=Hthirteencolor{coredata[H13_hyper]}] at ($(-0*\latWidth,-5*\latWidth)$) {{{coredata[H13_content]}}}; % H13
        \node [Assembly, fill=Gthirteencolor{coredata[G13_hyper]}] at ($( 1*\latWidth,-5*\latWidth)$) {{{coredata[G13_content]}}}; % G13
        \node [Assembly, fill=Fthirteencolor{coredata[F13_hyper]}] at ($( 2*\latWidth,-5*\latWidth)$) {{{coredata[F13_content]}}}; % F13
        \node [Assembly, fill=Ethirteencolor{coredata[E13_hyper]}] at ($( 3*\latWidth,-5*\latWidth)$) {{{coredata[E13_content]}}}; % E13
        \node [Assembly, fill=Dthirteencolor{coredata[D13_hyper]}] at ($( 4*\latWidth,-5*\latWidth)$) {{{coredata[D13_content]}}}; % D13
        \node [Assembly, fill=Cthirteencolor{coredata[C13_hyper]}] at ($( 5*\latWidth,-5*\latWidth)$) {{{coredata[C13_content]}}}; % C13
        \node [Assembly, fill=Bthirteencolor{coredata[B13_hyper]}] at ($( 6*\latWidth,-5*\latWidth)$) {{{coredata[B13_content]}}}; % B13

        \node [Assembly, fill=Hfourteencolor{coredata[H14_hyper]}] at ($(-0*\latWidth,-6*\latWidth)$) {{{coredata[H14_content]}}}; % H14
        \node [Assembly, fill=Gfourteencolor{coredata[G14_hyper]}] at ($( 1*\latWidth,-6*\latWidth)$) {{{coredata[G14_content]}}}; % G14
        \node [Assembly, fill=Ffourteencolor{coredata[F14_hyper]}] at ($( 2*\latWidth,-6*\latWidth)$) {{{coredata[F14_content]}}}; % F14
        \node [Assembly, fill=Efourteencolor{coredata[E14_hyper]}] at ($( 3*\latWidth,-6*\latWidth)$) {{{coredata[E14_content]}}}; % E14
        \node [Assembly, fill=Dfourteencolor{coredata[D14_hyper]}] at ($( 4*\latWidth,-6*\latWidth)$) {{{coredata[D14_content]}}}; % D14
        \node [Assembly, fill=Cfourteencolor{coredata[C14_hyper]}] at ($( 5*\latWidth,-6*\latWidth)$) {{{coredata[C14_content]}}}; % C14

        \node [Assembly, fill=Hfifteencolor{coredata[H15_hyper]}] at ($(-0*\latWidth,-7*\latWidth)$) {{{coredata[H15_content]}}}; % H15
        \node [Assembly, fill=Gfifteencolor{coredata[G15_hyper]}] at ($( 1*\latWidth,-7*\latWidth)$) {{{coredata[G15_content]}}}; % G15
        \node [Assembly, fill=Ffifteencolor{coredata[F15_hyper]}] at ($( 2*\latWidth,-7*\latWidth)$) {{{coredata[F15_content]}}}; % F15
        \node [Assembly, fill=Efifteencolor{coredata[E15_hyper]}] at ($( 3*\latWidth,-7*\latWidth)$) {{{coredata[E15_content]}}}; % E15

      \end{{tikzpicture}}
    }}

{legend}

    \caption{altcap}{{{caption} \label{{{label}}}}}
\end{{figure}}

"""






legend_t = r"""    % make the legend
    \begin{{tikzpicture}}
      \matrix [matrix of nodes]
          {{
              \node [Assembly, fill=\highenr, hyperlink node=mat_fuel31] at (0,0) {{}}; & \hyperref[mat_fuel31]{{3.1 w/o U235}}~~~ & \node [Assembly, fill=\midenr, hyperlink node=mat_fuel24] at (0,0) {{}}; & \hyperref[mat_fuel24]{{2.4 w/o U235}}~~~ \\
              \node [Assembly, fill=\lowenr, hyperlink node=mat_fuel16] at (0,0) {{}}; & \hyperref[mat_fuel16]{{1.6 w/o U235}}~~~ & ~~~ & ~~~\\
          }};
    \end{{tikzpicture}}"""

legend_t_c2 = r"""    % make the legend
    \begin{{tikzpicture}}
      \matrix [matrix of nodes]
          {{
              \node [Assembly, fill=\lowenr, hyperlink node=mat_fuel32] at (0,0) {{}}; & \hyperref[mat_fuel32]{{Fresh 3.2 w/o U235}}~~~ & \node [Assembly, fill=\highenr, hyperlink node=mat_fuel34] at (0,0) {{}}; & \hyperref[mat_fuel34]{{Fresh 3.4 w/o U235}}~~~ \\
              \node [Assembly, fill=\noenr] at (0,0) {{}}; & Shuffled Assembly~~~ & ~~~ & ~~~\\
          }};
    \end{{tikzpicture}}"""

hyper_t = r""", hyperlink node={target}"""


class CoreFig:
  def __init__(self,caption,label,altcap='',scale=1.0,scalebox=1.0,colorbyval=False,enlarged=False,fixedColorGradient=False):
    self.datadict = defaultdict(str)
    self.legend = ""
    self.caption = caption
    if altcap != '':
      self.altcap = '[{0}]'.format(altcap)
    else:
      self.altcap = ''
    self.label = label
    self.quarter = False
    self.structs = True
    self.scale=scale
    self.scalebox=scalebox
    self.colorbyval=colorbyval
    self.positions = copy.deepcopy(all_pos)
    self.values = []
    self.cycle2 = False
    self.enlarged=enlarged
    self.fixedColorGradient=False

  def set_quarter(self,sett):
    self.quarter = sett

  def set_structs(self,sett):
    self.structs = sett

  def set_legend(self):
    if self.cycle2:
      self.legend = legend_t_c2.format()
    else:
      self.legend = legend_t.format()

  def clear_legend(self):
    self.legend = ""

  def set_cycle_2(self, val):
    self.cycle2 = val

  def set_pos(self,pos,tex,hyper=None,val=None):
    """Set the tex in the tikz node at assembly position pos.

      args
        pos - Core position, e.g.: 'E15'
        tex - The tex to put in the node, e.g.  1.2//3.4//5.6   or  $\mathrm{S}_\mathrm{A}$, etc

     kwargs
        hyper - Default to none - name of a hypertarget for this node to link to

    """
    if not pos in self.positions: raise Exception("Unknown position {0}".format(pos))

    self.datadict[pos+"_content"] = tex
    if hyper:
      self.datadict[pos+"_hyper"] = hyper_t.format(target=hyper)

    if self.colorbyval:
      self.positions[pos] = val
      if val:
        self.values.append(val)


  def write_fig(self,filename):
    if self.quarter:
      if self.colorbyval:
        templ = quart_fig_clr_t
      else:
        if self.cycle2:
          templ = quart_fig_t_c2
        else:
          templ = quart_fig_t
    else:
      if self.colorbyval:
        templ = main_fig_clr_t
      else:
        if self.cycle2:
          templ = main_fig_t_c2
        else:
          templ = main_fig_t

    with open(filename,'w') as fh:

      if self.colorbyval:
        for pos,val in self.positions.items():
          p = pos.replace(pos[1:],numnames[pos[1:]])
          pocolkey = "{0}color".format(p)
          if not val:
            fh.write(color_t.format(colorname=pocolkey,r=1,g=1,b=1))
          else:
            if self.fixedColorGradient:
              min_val = -0.05
              max_val = 0.05
              if val < min_val:
                v = min_val
              elif val > max_val:
                v = max_val
              else:
                v = val
            else:
              v = val
              min_val = min(self.values)
              max_val = max(self.values)

            h = (1-(v-min_val)/(max_val - min_val))/3
            s = 0.8
            v = 0.8
            r,g,b = colorsys.hsv_to_rgb(h,s,v)
            fh.write(color_t.format(colorname=pocolkey,r=r,g=g,b=b))

      if self.enlarged:
        head_lhm = r"0.4*\RPVOR/\latWidth"
      else:
        head_lhm = r"\RPVOR/\latWidth"
      head_llm = "1"
      struct = ""

      if self.quarter:
        head_lhm = "1"
        head_llm = "0.6"

      if not self.structs:
        head_lhm = "1"
        head_llm = "0.6"
        struct = "%"

        if not self.quarter:
          head_lhm = "8.5"

      fh.write(templ.format(coredata=self.datadict,
                            legend=self.legend,
                            caption=self.caption,
                            altcap=self.altcap,
                            label=self.label,
                            scale=self.scale,
                            scalebox=self.scalebox,
                            head_lhm=head_lhm,
                            head_llm=head_llm,
                            struct=struct))

def main():

  fig = CoreFig('test caption','test label',scale=1.0,scalebox=0.8)
  fig.set_legend()
  fig.set_quarter(True)
  fig.set_pos('D11','test')
  fig.set_pos('D12','test2',hyper='mytarget')
  fig.write_fig('tmp.tex')

if __name__ == "__main__":
  main()
