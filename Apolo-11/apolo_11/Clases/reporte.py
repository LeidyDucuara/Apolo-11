import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import json

class Reporte:
    @staticmethod
    def Crear_reporte():
        log_path = os.path.join('Devices')

        def leer_archivos(path):
            logs = []
            for file in os.listdir(path):
                if file.endswith(".log"):
                    path_archivo = os.path.join('Devices', file)
                    with open(path_archivo) as fl:
                        jso_to_dic = json.load(fl)
                        logs.append(jso_to_dic)
            return logs

        data = leer_archivos(log_path)
        df = pd.DataFrame(data)
        df.columns = ['Fecha', 'Mision', 'Tipo', 'Estado', 'Id']

        # Definición de tablas
        cant_even_m_d = pd.crosstab(index=[df['Mision'], df['Tipo']], columns=df['Estado'], margins=True)
        dispos = df[df['Estado'] == 'unknown']
        dis_unk = pd.crosstab(dispos['Mision'], dispos['Tipo'], margins=True)
        kill = df[df['Estado'] == 'killed']
        dis_kill = pd.crosstab(kill['Mision'], kill['Estado'], margins=True)
        #dis_kill = dis_kill.drop(columns=['All'])
        #print("dis_kill", dis_kill)
        per_data = pd.crosstab(index=[df['Mision'], df['Tipo']], columns=df['Estado'],
                               margins=True).apply(lambda r: r / len(df) * 100,
                                                   axis=1)
        nombrearchivo='Reportes.pdf'
        ruta_archivo = os.path.join('Devices', nombrearchivo)
        with PdfPages(ruta_archivo) as pdf:
            plot = df['Mision'].value_counts().plot(kind='pie', autopct='%.2f',
                                                    figsize=(6, 6),
                                                    title='Analisis de dispositivos por Mision')
            pdf.savefig()
            plt.close()

            plot = df['Tipo'].value_counts().plot(kind='bar', title='Cantidad de dispositivos por Tipo')
            pdf.savefig()
            plt.close()

            plot = df['Tipo'].value_counts().plot(kind='pie', autopct='%.2f',
                                                        figsize=(6, 6),
                                                        title='Tipos de dispositivo en la ejecución')
            pdf.savefig()
            plt.close()

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.axis('off')
            tabla = ax.table(cellText=cant_even_m_d.values, colLabels=cant_even_m_d.columns, rowLabels=cant_even_m_d.index, loc='center')
            ax.text(0.5, 0.95, 'Analisis de por estado para cada mision y dispositivo:', transform=ax.transAxes, fontsize=16, ha='center')
            pdf.savefig(dpi=300, bbox_inches='tight')
            plt.close()

            for mision, group_df in df.groupby('Mision'):
                mis_est_mision = pd.crosstab(index=[group_df['Mision'], group_df['Tipo']], columns=group_df['Estado'])

                ax = mis_est_mision.plot(kind='bar', stacked=False, figsize=(12, 8))

                ax.set_title(f'Estados por Tipo de Dispositivo - {mision}')
                ax.set_xlabel('Tipo de Dispositivo')
                ax.set_ylabel('Cantidad')

                ax.legend(title='Estado', bbox_to_anchor=(1.05, 1), loc='upper left')
                ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
                pdf.savefig(dpi=300, bbox_inches='tight')
                plt.close()

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.axis('off')
            tabla = ax.table(cellText=dis_unk.values, colLabels=dis_unk.columns, rowLabels=dis_unk.index, loc='center')
            ax.text(0.5, 0.95, 'Dispositivos que presentan desconexiones:', transform=ax.transAxes, fontsize=16, ha='center')
            pdf.savefig()
            plt.close()

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.axis('off')
            tabla = ax.table(cellText=dis_kill.values, colLabels=dis_kill.columns, rowLabels=dis_kill.index, loc='center')
            ax.text(0.5, 0.95, 'Dispositivos inoperables:', transform=ax.transAxes, fontsize=16, ha='center')
            pdf.savefig()
            plt.close()

            fig, ax = plt.subplots(figsize=(16, 8))
            ax.axis('off')
            tabla = ax.table(cellText=per_data.values, colLabels=per_data.columns, rowLabels=per_data.index, loc='center')
            ax.text(0.5, 0.95, 'Calculo de porcentajes:', transform=ax.transAxes, fontsize=25, ha='center')
            pdf.savefig(dpi=400, bbox_inches='tight')
            plt.close()

