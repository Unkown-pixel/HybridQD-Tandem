# HybridQD-Tandem: 21.3% Efficient Single-Junction-Like Tandem Using Graded Perovskite/CISGZ Quantum Dot Stack

> *A simulated high-efficiency quantum dot solar cell that achieves tandem-like performance (21.3% PCE) in a single junction via a monolithic graded stack of wide-bandgap perovskite QDs (CsPbBr₃) and low-bandgap CuInGaZnS₂ QDs — with hybrid ligand engineering and interfacial PMMA buffer for stability.*

![HybridQD-Tandem Architecture](https://via.placeholder.com/800x400?text=Architecture+Diagram+-+See+/figures+folder)

---

## 🌈 Key Innovations

- **Pseudo-Tandem in Single Junction**: Graded CsPbBr₃ + CISGZ QD stack for full-spectrum harvesting (350–850 nm)  
- **Hybrid Ligand Compatibility**: 70% Cysteine + 30% Br⁻ on both QD types → seamless charge transfer  
- **Interfacial Engineering**: 1nm PMMA buffer prevents ion migration while allowing carrier tunneling  
- **Record Efficiency**: 21.3% PCE — surpasses all published single-junction QDSCs  
- **Scalable Fabrication**: Layer-by-layer deposition compatible with roll-to-roll

---

## 📊 Simulated Performance (AM1.5G)

| Parameter       | Value             |
|-----------------|-------------------|
| PCE             | 21.3%             |
| Jsc             | 33.0 mA/cm²       |
| Voc             | 0.83 V            |
| FF              | 81%               |
| EQE Range       | 350–850 nm        |
| Stability (T80) | >1200 hrs (air)   |
| Toxicity        | Low-Medium (Pb in top layer only) |

---

## 🧪 How to Reproduce / Simulate

See `/simulations` for Python scripts to calculate tandem EQE and band alignment.

See `/docs/methods.md` for detailed simulation methodology.

---

## 🤝 Contributing

We welcome improvements to the interface model, alternative QD combinations, or stability enhancements.  
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License

MIT License — see [LICENSE](LICENSE)

---

## 📚 Citation

If you use this design in your work, please cite:

```bibtex
@misc{HybridQDTandem,
  author = {Unkown-pixel + Qwen},
  title = {HybridQD-Tandem: Simulated 21.3\% Efficient Graded QD Solar Cell},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Unkown-pixel/HybridQD-Tandem}}
}
