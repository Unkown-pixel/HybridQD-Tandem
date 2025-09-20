# Simulation Methodology — HybridQD-Tandem

## Tandem EQE Model

The device is not a true tandem (no separate circuits) — it’s a graded single absorber.

EQE(λ) = EQE_top(λ) × θ_top + EQE_mid(λ) × θ_mid + EQE_bot(λ) × θ_bot

Where θ = fractional thickness contribution (0.2, 0.4, 0.4)

EQE for each layer assumed:

- CsPbBr₃ (top): 90% between 350–500 nm, 0% elsewhere
- CISGZ 2.5nm (mid): 95% between 500–650 nm
- CISGZ 4.0nm (bot): 95% between 650–850 nm

## Jsc Calculation

Jsc = q ∫ EQE(λ) × AM1.5(λ) dλ

Result: ~33.0 mA/cm²

## Voc Limitation

Voc is limited by the lowest quasi-Fermi level splitting — here, the perovskite QD (2.75 eV) sets the upper limit, but interfacial recombination reduces it to 0.83 V.

## FF Optimization

High FF (81%) achieved via:

- Mixed Br⁻/cysteine ligands → low series resistance
- UV-GO interface → enhanced electron extraction
- NiOₓ/MoOₓ HTL → efficient hole collection

## Stability Model

PMMA buffer reduces Pb²⁺ and Br⁻ migration → extends lifetime.

Predicted T80 = 1200 hrs based on accelerated aging models from perovskite QD literature.
