\version "2.20.0"

\language "english"

\header {
  title = "For All The Saints"
}

violin = {
  \relative c' {
    \time 4/4
    \key g \major
    \tempo 2 = 80
    r4 d' b a |
    g2. d4 e g a d, |
    b'2. b4 |
    a2 a4 g |
    fs2 fs |
    g4 a fs e |
    d2. d4 |
    g2 g4 g |
    d'2. d4 |
    c d c8 b a g |
    a2 d |
    e4 d8 c d2 |
    g,2. a8 b |
    c4 b a2 |
    g1
  }
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } { \transpose g ef \violin }
  \layout {}
  \midi {}
}
