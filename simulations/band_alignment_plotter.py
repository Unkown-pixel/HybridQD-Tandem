# Band Alignment Plotter for HybridQD-Tandem Stack

import matplotlib.pyplot as plt

# Energy levels in eV (vs vacuum)
materials = {
    'CsPbBr3 QD': {'LUMO': -3.6, 'HOMO': -6.35},
    'CISGZ QD': {'LUMO': -3.8, 'HOMO': -5.45},
    'ZnMgO ETL': {'CBM': -3.9, 'VBM': -7.2},
    'NiOx HTL': {'CBM': -1.8, 'VBM': -5.4}
}

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# Plot energy levels
for i, (mat, levels) in enumerate(materials.items()):
    ax.plot([i, i], [levels['LUMO'], levels['HOMO']], 'k-', linewidth=4, label=mat)
    ax.text(i, levels['LUMO'] + 0.1, f"LUMO\n{levels['LUMO']} eV", ha='center')
    ax.text(i, levels['HOMO'] - 0.2, f"HOMO\n{levels['HOMO']} eV", ha='center')

ax.set_xlim(-0.5, len(materials)-0.5)
ax.set_ylim(-7.5, -1.5)
ax.set_ylabel('Energy (eV vs Vacuum)')
ax.set_title('Band Alignment in HybridQD-Tandem')
ax.grid(True, alpha=0.3)
ax.set_xticks(range(len(materials)))
ax.set_xticklabels(materials.keys(), rotation=45)
plt.tight_layout()
plt.savefig('band_alignment.png', dpi=300, bbox_inches='tight')
plt.show()

print("Band alignment plot saved as 'band_alignment.png'")
print("Note: Small LUMO offset (0.2 eV) between CsPbBr3 and CISGZ allows electron transfer with minimal loss.")
print("HOMO alignment between CISGZ and NiOx is near-perfect → efficient hole extraction.")
