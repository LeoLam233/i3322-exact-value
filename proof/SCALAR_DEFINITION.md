# Exact analytic residual

This is an exposition of surviving component E's `SYMBOLIC_DERIVATION.md`, `LOCAL_MANIFOLD_CERTIFICATE.md`, `SCALAR_REDUCTION.md`, and `GLOBAL_UNIQUENESS.md`, as presented in manuscript Section 6. The source locators are in [FROZEN_PATHS.md](../machine/FROZEN_PATHS.md). It supplies the meaning of the unique-root characterization, not a new proof or modified certificate.

For `s ∈ I`, use

\[
a(s)=\sqrt{\frac{4s+5+\sqrt{16s^2+24s-7}}8},\quad
T=a(I),\quad \sigma(t)=\frac{4t^4-5t^2+2}{4t^2-1}.
\]

Put `b(c)=sqrt(1-c²)/2`, `B_0(c)=(1-c²)/4`, and `d(x,y)=xy+(x-y)/2-1`.
For the canonical state `(x,y,u)`, with `u=λ_j/λ_(j-1)`, the rational coordinate is `q=s-d(x,y)-b(x)/u`. On complete valid chains, `q>0` and `qbar=s-d(x,y)-q>0`. The inverse reconstructs `u=b(x)/qbar`.

\[
\widehat F_s(x,y,q)=(y,z,Q),\quad
z=\frac{y}{2q}-\frac{(x-1/2)B_0(y)}{q^2}-\frac12,\quad
Q=s-d(y,z)-\frac{B_0(y)}q.
\]

Define

\[
G(t)=\frac{(2t-1)(t+1)}{2(2t+1)},\quad
A=(t+1)(2t-1)^2,\quad C=(1-t)(2t+1)^2,\quad D=4t^2(4t^2-1),
\]

\[
\mu(t)=\frac{D+\sqrt{D^2-4AC}}{2A}.
\]

The analytic invariant germ `P(t,ζ)` is fixed by

\[
P(t,0)=(t,t,G(t)),\quad P_\zeta(t,0)=(-1/\mu,-1,t-1/2),\quad
P(t,\mu\zeta)=\widehat F_{\sigma(t)}(P(t,\zeta)).
\]

Let `W(t,ζ)=Fhat_(σ(t))^5 P(t,ζ)=(x(t,ζ),y(t,ζ),q(t,ζ))` on the certified valid continuation. The complete independent phase envelope is `[0.000078125,0.0025]²`. Let `φ(t)` be the unique analytic phase in `[0.0005,0.0007]` satisfying `x(t,φ)+y(t,φ)=0`. Define

\[
\mathcal R(t)=2q(t,\phi(t))-\sigma(t)+d(x(t,\phi(t)),y(t,\phi(t))).
\]

Only after complete independent-phase coverage and exclusion of asymmetric full matches does E prove `Rcal(t)=0` if and only if `M_(σ(t))` is nonempty, on all `T`. Its derivative is strictly positive on the full outward parameter enclosure and its clean endpoint residual signs are opposite. Therefore the unique zero defines `s_*` through `σ`.

The degree-36 and degree-48 polynomials enclose the same exactly defined analytic germ with rigorously bounded remainders and derivatives. They are not substituted for `P` in the theorem. The definition does not assume that two phases are equal; the equality is a conclusion of the exhaustive O6 argument. See [audit priorities](../AUDIT_ME_FIRST.md).
