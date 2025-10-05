# dashboard_defense_sri_lanka_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Sri Lanka",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #8D0034, #FFB400, #00534E, #6A0C49);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #8D0034, #6A0C49);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #8D0034;
        border-bottom: 3px solid #FFB400;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .special-forces-card {
        background: linear-gradient(135deg, #00534E, #008080);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .navy-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .air-force-card {
        background: linear-gradient(135deg, #008080, #00CED1);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .army-card {
        background: linear-gradient(135deg, #8D0034, #B22222);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .coast-guard-card {
        background: linear-gradient(135deg, #228B22, #32CD32);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseSriLankaDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.naval_assets = self.define_naval_assets()
        self.air_assets = self.define_air_assets()
        
    def define_branches_options(self):
        return [
            "Forces Armées Sri Lankaises", "Armée de Terre", "Marine Sri Lankaise", 
            "Force Aérienne Sri Lankaise", "Garde Côtière", "Forces Spéciales",
            "Police Militaire", "Unité Anti-Terroriste"
        ]
    
    def define_programmes_options(self):
        return [
            "Modernisation des Forces", "Défense Côtière", "Surveillance Maritime",
            "Lutte Anti-Terroriste", "Coopération Régionale", "Cybersécurité"
        ]
    
    def define_naval_assets(self):
        return {
            "Navire d'attaque rapide Nandimithra": {"type": "Patrouilleur", "tonnage": 250, "armement": "Canons 30mm", "annee": 2014},
            "Frégate SLNS Sayura": {"type": "Frégate", "tonnage": 2200, "armement": "Canons 76mm", "annee": 2000},
            "Patrouilleur Sagara": {"type": "Patrouilleur", "tonnage": 350, "armement": "Canons 23mm", "annee": 2015},
            "Vedette rapide Weeraya": {"type": "Vedette", "tonnage": 55, "armement": "Mitrailleuses", "annee": 2018},
            "Navire de débarquement SLNS Shakthi": {"type": "Transport", "tonnage": 4100, "armement": "Canons 40mm", "annee": 1994}
        }
    
    def define_air_assets(self):
        return {
            "F-7G Skybolt": {"type": "Chasseur", "vitesse": "Mach 2.0", "armement": "Missiles air-air", "annee": 2008},
            "K-8 Karakorum": {"type": "Entraînement/Attaque", "vitesse": "800 km/h", "armement": "Canon 23mm", "annee": 2011},
            "Mi-24 Hind": {"type": "Hélicoptère de combat", "vitesse": "335 km/h", "armement": "Rockets + Canon", "annee": 2000},
            "C-130 Hercules": {"type": "Transport", "vitesse": "540 km/h", "capacite": "20 tonnes", "annee": 2000},
            "Beechcraft B200": {"type": "Surveillance", "vitesse": "500 km/h", "rayon": "2000 km", "annee": 2010}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour le Sri Lanka"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Patrouilles_Maritimes': self.simulate_maritime_patrols(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Artillerie': self.simulate_artillery_capacity(annees),
            'Couverture_Radar': self.simulate_radar_coverage(annees),
            'Resilience_Logistique': self.simulate_logistical_resilience(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Munitions': self.simulate_ammunition_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'maritime' in config.get('priorites', []):
            data.update({
                'Navires_Patrouille': self.simulate_naval_fleet(annees),
                'Portee_Surveillance_Nm': self.simulate_surveillance_range(annees),
                'Interceptions_Maritimes': self.simulate_maritime_interceptions(annees),
                'Exercices_Combines': self.simulate_joint_exercises(annees)
            })
        
        if 'aerien' in config.get('priorites', []):
            data.update({
                'Heures_Vol_Combat': self.simulate_flight_hours(annees),
                'Taux_Disponibilite_Avions': self.simulate_aircraft_availability(annees),
                'Couverture_AD': self.simulate_air_defense(annees)
            })
        
        if 'cyber' in config.get('priorites', []):
            data.update({
                'Attaques_Cyber_Reussies': self.simulate_cyber_attacks(annees),
                'Reseau_Commandement_Cyber': self.simulate_cyber_command(annees),
                'Cyber_Defense_Niveau': self.simulate_cyber_defense(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour le Sri Lanka"""
        configs = {
            "Forces Armées Sri Lankaises": {
                "type": "armee_totale",
                "budget_base": 1.8,
                "personnel_base": 350,
                "exercices_base": 45,
                "priorites": ["maritime", "aerien", "terrestre", "cyber", "antiterrorisme"],
                "doctrines": ["Défense Intégrée", "Coopération Régionale", "Lutte Asymétrique"],
                "capacites_speciales": ["Contre-Insurrection", "Opérations Côtières", "Forces Spéciales"]
            },
            "Marine Sri Lankaise": {
                "type": "branche_navale",
                "personnel_base": 48,
                "exercices_base": 25,
                "priorites": ["surveillance_eez", "lutte_piraterie", "defense_cotiere"],
                "navires_principaux": ["Frégates", "Patrouilleurs", "Vedettes rapides"],
                "zones_operations": ["Océan Indien", "Golfe du Bengale", "Détroit de Palk"]
            },
            "Force Aérienne Sri Lankaise": {
                "type": "branche_aerienne",
                "personnel_base": 28,
                "exercices_base": 20,
                "priorites": ["defense_aerienne", "surveillance", "appui_sol"],
                "avions_principaux": ["F-7G", "K-8", "Mi-24", "C-130"],
                "bases_principales": ["Katunayake", "China Bay", "Anuradhapura"]
            },
            "Modernisation des Forces": {
                "type": "programme_strategique",
                "budget_base": 0.4,
                "priorites": ["equipements_terrestres", "systemes_navals", "avions_combat"],
                "acquisitions_recentes": ["Radars côtiers", "Systèmes de communication", "Véhicules blindés"],
                "objectifs": "Forces professionnelles et mobiles"
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 50,
            "exercices_base": 15,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 1.5)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.025 * (annee - 2000))
            # Variations selon événements
            if 2006 <= annee <= 2009:  # Période de conflit
                base *= 1.25
            elif 2010 <= annee <= 2014:  # Reconstruction post-conflit
                base *= 0.9
            elif annee >= 2019:  # Modernisation
                base *= 1.1
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 200)
        return [personnel_base * (1 + 0.005 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [2.8 + 0.1 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 25)
        return [base + 2 * (annee - 2000) + 3 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 60 + 1.2 * (annee - 2000)
            if annee >= 2009:  # Post-conflit
                base += 10
            if annee >= 2015:  # Professionnalisation
                base += 5
            readiness.append(min(base, 90))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            if annee < 2009:
                base = 40  # Conflit interne
            elif annee < 2015:
                base = 55  # Reconstruction
            else:
                base = 70 + 1.5 * (annee - 2015)  # Modernisation
            deterrence.append(min(base, 85))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(96 - 1.5 * (annee - 2000), 48) for annee in annees]
    
    def simulate_maritime_patrols(self, annees):
        """Patrouilles maritimes"""
        patrols = []
        for annee in annees:
            if annee < 2009:
                patrols.append(150 + 10 * (annee - 2000))
            elif annee < 2015:
                patrols.append(300 + 15 * (annee - 2009))
            else:
                patrols.append(450 + 20 * (annee - 2015))
        return [min(p, 800) for p in patrols]
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(40 + 2.5 * (annee - 2000), 80) for annee in annees]
    
    def simulate_artillery_capacity(self, annees):
        """Capacité d'artillerie"""
        return [min(65 + 1.8 * (annee - 2000), 88) for annee in annees]
    
    def simulate_radar_coverage(self, annees):
        """Couverture radar"""
        return [min(45 + 2.8 * (annee - 2000), 85) for annee in annees]
    
    def simulate_logistical_resilience(self, annees):
        """Résilience logistique"""
        return [min(55 + 2.2 * (annee - 2000), 87) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(35 + 3.5 * (annee - 2000), 82) for annee in annees]
    
    def simulate_ammunition_production(self, annees):
        """Production de munitions (indice)"""
        return [min(50 + 2.5 * (annee - 2000), 85) for annee in annees]
    
    def simulate_naval_fleet(self, annees):
        """Évolution de la flotte navale"""
        fleet = []
        for annee in annees:
            if annee < 2005:
                fleet.append(40 + (annee - 2000))
            elif annee < 2010:
                fleet.append(50 + 2 * (annee - 2005))
            else:
                fleet.append(65 + 3 * (annee - 2010))
        return [min(f, 120) for f in fleet]
    
    def simulate_surveillance_range(self, annees):
        """Portée de surveillance maritime"""
        return [min(50 + 4 * (annee - 2000), 200) for annee in annees]
    
    def simulate_maritime_interceptions(self, annees):
        """Interceptions maritimes réussies"""
        return [min(20 + 3 * (annee - 2000), 150) for annee in annees]
    
    def simulate_joint_exercises(self, annees):
        """Exercices combinés avec partenaires"""
        return [min(5 + 2 * (annee - 2000), 40) for annee in annees]
    
    def simulate_flight_hours(self, annees):
        """Heures de vol de combat"""
        return [min(800 + 50 * (annee - 2000), 2000) for annee in annees]
    
    def simulate_aircraft_availability(self, annees):
        """Taux de disponibilité des avions"""
        return [min(60 + 1.5 * (annee - 2000), 85) for annee in annees]
    
    def simulate_air_defense(self, annees):
        """Défense anti-aérienne"""
        return [min(40 + 2.5 * (annee - 2000), 80) for annee in annees]
    
    def simulate_cyber_attacks(self, annees):
        """Attaques cyber réussies (estimation)"""
        return [max(3 + 1.5 * (annee - 2010), 0) for annee in annees]
    
    def simulate_cyber_command(self, annees):
        """Réseau de commandement cyber"""
        return [min(30 + 4 * (annee - 2010), 85) for annee in annees]
    
    def simulate_cyber_defense(self, annees):
        """Capacités de cyber défense"""
        return [min(40 + 3.5 * (annee - 2010), 82) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🦁 ANALYSE STRATÉGIQUE AVANCÉE - SRI LANKA</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #8D0034, #FFB400); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🏝️ SYSTÈME DE DÉFENSE INTÉGRÉ DE LA RÉPUBLIQUE DÉMOCRATIQUE SOCIALISTE DU SRI LANKA</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et stratégiques (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Branche Militaire", "Programmes Stratégiques", "Vue Systémique", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Analyse Branche Militaire":
            selection = st.sidebar.selectbox("Branche militaire:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Vue Systémique":
            selection = "Forces Armées Sri Lankaises"
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_doctrinal = st.sidebar.checkbox("Analyse doctrinale", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo", "Tensions Régionales", "Modernisation Accélérée", "Crise Maritime"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_doctrinal': show_doctrinal,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ +{:.1f}% depuis 2000</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 
                     ((data_actuelle['Personnel_Milliers'] - data_2000['Personnel_Milliers']) / data_2000['Personnel_Milliers']) * 100), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="navy-card">
                <h4>⚓ CAPACITÉ NAVALE</h4>
                <h2>{:.0f}%</h2>
                <p>🚢 {} patrouilles/an</p>
            </div>
            """.format(data_actuelle['Capacite_Dissuasion'], 
                     int(data_actuelle.get('Patrouilles_Maritimes', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="air-force-card">
                <h4>✈️ CAPACITÉS AÉRIENNES</h4>
                <h2>{:.0f}%</h2>
                <p>🛩️ {} heures de vol</p>
            </div>
            """.format(data_actuelle.get('Couverture_AD', 0), 
                     int(data_actuelle.get('Heures_Vol_Combat', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_radar = ((data_actuelle['Couverture_Radar'] - data_2000['Couverture_Radar']) / 
                              data_2000['Couverture_Radar']) * 100
            st.metric(
                "📡 Couverture Radar",
                f"{data_actuelle['Couverture_Radar']:.1f}%",
                f"{croissance_radar:+.1f}%"
            )
        
        with col7:
            if 'Portee_Surveillance_Nm' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Surveillance_Nm'] - data_2000.get('Portee_Surveillance_Nm', 50)) / 
                                   data_2000.get('Portee_Surveillance_Nm', 50)) * 100
                st.metric(
                    "🌊 Portée Surveillance",
                    f"{data_actuelle['Portee_Surveillance_Nm']:,.0f} nm",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Couverture_Radar']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Couverture Radar']
            couleurs = ['#8D0034', '#FFB400', '#00534E', '#6A0C49']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des programmes stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Patrouilles_Maritimes' in df.columns:
                strategic_data.append(df['Patrouilles_Maritimes'])
                strategic_names.append('Patrouilles Maritimes')
            
            if 'Navires_Patrouille' in df.columns:
                strategic_data.append(df['Navires_Patrouille'])
                strategic_names.append('Flotte Navale')
            
            if 'Heures_Vol_Combat' in df.columns:
                strategic_data.append(df['Heures_Vol_Combat'] / 10)  # Normalisation
                strategic_names.append('Heures Vol (x10)')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 PROGRAMMES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Cartes des zones d'influence
            st.markdown("""
            <div class="special-forces-card">
                <h4>🎯 ZONES STRATÉGIQUES MARITIMES</h4>
                <p><strong>Zone Économique Exclusive:</strong> 200,000 km²</p>
                <p><strong>Détroit de Palk:</strong> Séparation avec l'Inde</p>
                <p><strong>Océan Indien:</strong> Route maritime vitale</p>
                <p><strong>Port de Colombo:</strong> Hub régional</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="army-card">
                <h4>🤝 RELATIONS INTERNATIONALES</h4>
                <p><strong>Inde:</strong> Partenaire stratégique majeur</p>
                <p><strong>Chine:</strong> Investissements infrastructurels</p>
                <p><strong>USA:</strong> Coopération maritime</p>
                <p><strong>Japon:</strong> Aide au développement</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des défis sécuritaires
            challenges_data = {
                'Année': [2000, 2005, 2009, 2014, 2019, 2023],
                'Niveau_Defi': [8, 9, 10, 4, 5, 6],  # sur 10
                'Type_Defi': ['Conflit Civil', 'Conflit Civil', 'Fin Conflit', 'Reconstruction', 'Stabilité', 'Défis Maritimes']
            }
            challenges_df = pd.DataFrame(challenges_data)
            
            fig = px.line(challenges_df, x='Année', y='Niveau_Defi', 
                         title="📉 ÉVOLUTION DES DÉFIS SÉCURITAIRES",
                         labels={'Niveau_Defi': 'Niveau de Défi'},
                         markers=True)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Indice de stabilité
            stabilite = [min(30 + 3 * (annee - 2000), 85) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=stabilite,
                         title="🕊️ INDICE DE STABILITÉ NATIONALE",
                         labels={'x': 'Année', 'y': 'Niveau de Stabilité (%)'})
            fig.update_traces(fillcolor='rgba(141, 0, 52, 0.3)', line_color='#8D0034')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['F-7G Skybolt', 'K-8 Karakorum', 'Mi-24 Hind', 
                           'Navire Nandimithra', 'Frégate Sayura', 'Radar côtier'],
                'Portée (km)': [1800, 800, 450, 2000, 4000, 300],
                'Année Service': [2008, 2011, 2000, 2014, 2000, 2015],
                'Statut': ['Opérationnel', 'Opérationnel', 'Modernisation', 'Opérationnel', 'Service', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Année Service', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation
            modernization_data = {
                'Domaine': ['Forces Terrestres', 'Marine', 
                          'Force Aérienne', 'Cybersécurité', 'Renseignement'],
                'Niveau 2000': [50, 40, 45, 20, 35],
                'Niveau 2027': [75, 70, 72, 65, 68]
            }
            modern_df = pd.DataFrame(modernization_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=modern_df['Domaine'], y=modern_df['Niveau 2000'],
                                marker_color='#8D0034'))
            fig.add_trace(go.Bar(name='2027', x=modern_df['Domaine'], y=modern_df['Niveau 2027'],
                                marker_color='#FFB400'))
            
            fig.update_layout(title="📈 MODERNISATION DES CAPACITÉS MILITAIRES",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des installations
            st.markdown("""
            <div class="coast-guard-card">
                <h4>🗺️ INSTALLATIONS STRATÉGIQUES CLÉS</h4>
                <p><strong>Port de Colombo:</strong> Base navale principale</p>
                <p><strong>Base Aérienne Katunayake:</strong> QG Force Aérienne</p>
                <p><strong>Trincomalee:</strong> Port en eaux profondes</p>
                <p><strong>Hambantota:</strong> Port stratégique</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="special-forces-card">
                <h4>🎯 DÉFENSE MULTIDIMENSIONNELLE</h4>
                <p><strong>Approche intégrée:</strong> Terre, mer, air, cyber</p>
                <p><strong>Flexibilité:</strong> Adaptation aux menaces</p>
                <p><strong>Coordination:</strong> Action interarmées</p>
                <p><strong>Résilience:</strong> Capacité de récupération</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="navy-card">
                <h4>🌊 DOCTRINE MARITIME</h4>
                <p><strong>Surveillance EEZ:</strong> Protection zone économique</p>
                <p><strong>Lutte piraterie:</strong> Sécurité routes maritimes</p>
                <p><strong>Coopération:</strong> Exercices internationaux</p>
                <p><strong>Défense côtière:</strong> Protection territoire</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="air-force-card">
                <h4>✈️ STRATÉGIE AÉRIENNE</h4>
                <p><strong>Défense aérienne:</strong> Couverture territoire</p>
                <p><strong>Appui sol:</strong> Support forces terrestres</p>
                <p><strong>Surveillance:</strong> Monitoring maritime</p>
                <p><strong>Transport:</strong> Mobilité stratégique</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="army-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DES FORCES ARMÉES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Unité de commandement:</strong> Coordination centralisée</div>
                <div><strong>• Mobilité et rapidité:</strong> Réponse aux crises</div>
                <div><strong>• Utilisation du terrain:</strong> Avantage géographique</div>
                <div><strong>• Coopération interarmées:</strong> Synergie des forces</div>
                <div><strong>• Professionnalisme:</strong> Forces entraînées</div>
                <div><strong>• Préparation logistique:</strong> Soutien continu</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Terrorisme Maritime', 'Trafic Illégal', 'Tensions Frontalières', 
                                 'Cyber Attaque', 'Ingérence Étrangère', 'Instabilité Régionale'],
                'Probabilité': [0.6, 0.8, 0.4, 0.7, 0.5, 0.3],
                'Impact': [0.7, 0.6, 0.8, 0.5, 0.7, 0.6],
                'Niveau Préparation': [0.8, 0.7, 0.6, 0.5, 0.4, 0.5]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Crise Maritime', 'Trafic Drogues', 'Cyber Attaque', 
                           'Tensions Frontalières', 'Catastrophe Naturelle'],
                'Marine': [0.9, 0.8, 0.2, 0.4, 0.7],
                'Air': [0.7, 0.3, 0.1, 0.8, 0.6],
                'Terre': [0.4, 0.6, 0.3, 0.9, 0.8]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Marine', x=response_df['Scénario'], y=response_df['Marine']),
                go.Bar(name='Air', x=response_df['Scénario'], y=response_df['Air']),
                go.Bar(name='Terre', x=response_df['Scénario'], y=response_df['Terre'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR SCÉNARIO",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="special-forces-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Renforcement naval:</strong> Patrouilleurs avancés</div>
                <div><strong>• Modernisation aérienne:</strong> Radars et intercepteurs</div>
                <div><strong>• Surveillance côtière:</strong> Systèmes intégrés</div>
                <div><strong>• Capacités cyber:</strong> Défense numérique</div>
                <div><strong>• Forces spéciales:</strong> Réponse rapide</div>
                <div><strong>• Coopération régionale:</strong> Exercices conjoints</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_naval_database(self):
        """Base de données des actifs navals"""
        st.markdown('<h3 class="section-header">⚓ BASE DE DONNÉES DES ACTIFS NAVALS</h3>', 
                   unsafe_allow_html=True)
        
        naval_data = []
        for nom, specs in self.naval_assets.items():
            naval_data.append({
                'Navire': nom,
                'Type': specs['type'],
                'Tonnage': specs['tonnage'],
                'Armement Principal': specs['armement'],
                'Année Service': specs['annee'],
                'Statut': 'Opérationnel' if specs['annee'] > 2000 else 'Modernisation'
            })
        
        naval_df = pd.DataFrame(naval_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(naval_df, x='Tonnage', y='Année Service',
                           size='Tonnage', color='Type',
                           hover_name='Navire', log_x=True,
                           title="⚓ CARACTÉRISTIQUES DE LA FLOTTE NAVALE",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="navy-card">
                <h4>📋 INVENTAIRE NAVAL</h4>
            """, unsafe_allow_html=True)
            
            for navire in naval_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{navire['Navire']}</strong><br>
                    ⚓ {navire['Type']} • 🚢 {navire['Tonnage']} t<br>
                    🎯 {navire['Armement Principal']}<br>
                    📅 {navire['Année Service']} • {navire['Statut']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "📚 Doctrine Militaire",
            "⚠️ Évaluation Menaces",
            "⚓ Actifs Navals",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_doctrinal']:
                self.create_doctrinal_analysis(config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_naval_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - SRI LANKA</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="special-forces-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="navy-card" style="margin: 0.5rem 0;">
                        <strong>🌊 Position Géostratégique</strong>
                        <p>Localisation clé sur les routes maritimes de l'Océan Indien</p>
                    </div>
                    <div class="air-force-card" style="margin: 0.5rem 0;">
                        <strong>🎯 Expérience Opérationnelle</strong>
                        <p>Forces aguerries par des décennies d'opérations de contre-insurrection</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🤝 Coopération Internationale</strong>
                        <p>Partenariats stratégiques avec grandes puissances régionales</p>
                    </div>
                    <div class="coast-guard-card" style="margin: 0.5rem 0;">
                        <strong>🛡️ Connaissance du Terrain</strong>
                        <p>Maîtrise parfaite du territoire national et des zones côtières</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="army-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>💸 Contraintes Budgétaires</strong>
                        <p>Ressources limitées pour la modernisation des équipements</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🔧 Dépendance Technologique</strong>
                        <p>Équipements majoritairement d'origine étrangère</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Enjeux Maritimes</strong>
                        <p>Vaste ZEE à surveiller avec moyens limités</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Menaces Asymétriques</strong>
                        <p>Risques de terrorisme et trafics illicites</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🌊 DOMAINE MARITIME</h5>
                    <p>• Patrouilleurs avancés<br>• Systèmes de surveillance<br>• Coopération régionale<br>• Lutte anti-piraterie</p>
                </div>
                <div>
                    <h5>✈️ DOMAINE AÉRIEN</h5>
                    <p>• Modernisation chasseurs<br>• Radars avancés<br>• Drones de surveillance<br>• Transport stratégique</p>
                </div>
                <div>
                    <h5>💻 DOMAINE CYBER</h5>
                    <p>• Cyber défense<br>• Guerre électronique<br>• Renseignement numérique<br>• Protection infrastructures</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="special-forces-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ DÉFENSE ACTIVE</h5>
                    <p>• Renforcement capacités maritimes<br>
                    • Modernisation systèmes aériens<br>
                    • Développement cyber défense<br>
                    • Professionnalisation forces</p>
                </div>
                <div>
                    <h5>🤝 COOPÉRATION RÉGIONALE</h5>
                    <p>• Partenariats stratégiques<br>
                    • Exercices combinés<br>
                    • Échange de renseignements<br>
                    • Sécurité collective</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseSriLankaDashboardAvance()
    dashboard.run_advanced_dashboard()