import matplotlib.pyplot as plt

# Nombres de las categorías
categorias = ["All", "Self-direction: thought", "Self-direction: action", 
             "Stimulation", "Hedonism", "Achievement", "Power: dominance", 
             "Power: resources", "Face", "Security: personal", "Security: societal", 
             "Tradition", "Conformity: rules", "Conformity: interpersonal", 
             "Humility", "Benevolence: caring", "Benevolence: dependability", 
             "Universalism: concern", "Universalism: nature", "Universalism: tolerance", 
             "Universalism: objectivity"]

# F1-score del BERT en gris y Ensemble(v1) en azul para cada categoría
bert_gris_scores = [.42, .44, .55, .05, .20, .56, .29, .44, .13, .74, .59, 
                    .43, .47, .23, .07, .46, .14, .67, .71, .32, .33]
ensemble_azul_scores = [.47, .44, .61, .25, .27, .59, .33, .45, .30, .73, .59, 
                        .49, .53, .29, .21, .48, .29, .69, .70, .43, .55]

# Configuración del gráfico
bar_width = 0.35
index = range(len(categorias))
color = "#6d6af7"

fig, ax = plt.subplots(figsize=(12, 7))
bar1 = ax.bar(index, bert_gris_scores, bar_width, label='BERT', color=color)
bar2 = ax.bar([i+bar_width for i in index], ensemble_azul_scores, bar_width, label='Ensemble(v1)', color=color)

# Ajuste de ejes y leyenda
ax.set_xlabel('Categoría')
ax.set_ylabel('F1-score')
ax.set_title('Comparación F1-score entre BERT (gris) y Ensemble(v1) (azul)')
ax.set_xticks([i+bar_width for i in index])
ax.set_xticklabels(categorias, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()
