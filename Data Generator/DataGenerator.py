import random
import pandas as pd
import numpy as np
from typing import List, Dict

class SlayTheSpireDataGenerator:
    def __init__(self, num_players=1000):
        self.num_players = num_players
        self.data = []
        self.characters = ['Ironclad', 'Silent', 'Defect', 'Watcher']
        self.ascension_levels = list(range(1, 21))

    def generate_player_profile(self) -> Dict:
        """Generate a player profile mimicking Slay the Spire mechanics"""
        return {
            'player_id': random.randint(1000, 9999),
            'character': random.choice(self.characters),
            'ascension_level': random.choice(self.ascension_levels),
            'total_runs': random.randint(10, 500),
            'max_score': random.randint(500, 5000),
            'win_streak': random.randint(0, 20)
        }

    def simulate_run(self, player_profile: Dict) -> Dict:
        """Simulate a Slay the Spire-like game run"""
        # Adjust difficulty based on ascension level
        base_hp_loss = max(10, player_profile['ascension_level'] * 2)
        
        run_data = {
            'player_id': player_profile['player_id'],
            'character': player_profile['character'],
            'ascension_level': player_profile['ascension_level'],
            'run_id': random.randint(10000, 99999),
            
            # Card-related metrics
            'cards_obtained': random.randint(15, 50),
            'card_removal_count': random.randint(0, 5),
            'card_upgrade_count': random.randint(0, 10),
            
            # Combat and health metrics
            'elites_defeated': random.randint(0, 4),
            'boss_defeated': random.choice([True, False]),
            'starting_hp': 80,
            'max_hp_gain': random.randint(0, 30),
            'hp_loss_on_damage': random.randint(base_hp_loss, base_hp_loss * 2),
            
            # Relics and events
            'relics_collected': random.randint(0, 10),
            'events_encountered': random.randint(1, 10),
            
            # Score and progression
            'floor_reached': random.randint(20, 60),
            'gold_collected': random.randint(100, 1000),
            
            # Outcome
            'run_outcome': random.choices(['win', 'lose'], weights=[0.2, 0.8])[0]
        }
        
        # Adjust final score based on run outcome and ascension level
        base_score = (run_data['floor_reached'] * 50) + (run_data['gold_collected'])
        run_data['final_score'] = base_score if run_data['run_outcome'] == 'win' else base_score // 2
        
        return run_data

    def generate_dataset(self) -> pd.DataFrame:
        """Generate comprehensive game dataset"""
        for _ in range(self.num_players):
            player_profile = self.generate_player_profile()
            num_runs = random.randint(5, 50)
            
            for _ in range(num_runs):
                run_data = self.simulate_run(player_profile)
                run_data.update(player_profile)
                self.data.append(run_data)
        
        return pd.DataFrame(self.data)

    def analyze_dataset(self, df):
        """Perform Slay the Spire-specific analysis"""
        # Calculate win rates per character correctly
        character_win_rates = df.groupby('character')['run_outcome'].apply(
            lambda x: (x == 'win').mean()
        ).to_dict()
        
        # Calculate win rates per ascension level
        ascension_win_rates = df.groupby('ascension_level')['run_outcome'].apply(
            lambda x: (x == 'win').mean()
        ).to_dict()
        
        analysis = {
            'total_players': df['player_id'].nunique(),
            'total_runs': len(df),
            'character_win_rates': character_win_rates,
            'average_floor_reached': df['floor_reached'].mean(),
            'ascension_level_performance': ascension_win_rates,
            'avg_relics_per_run': df['relics_collected'].mean(),
            'avg_cards_obtained': df['cards_obtained'].mean(),
            'max_score_overall': df['final_score'].max()
        }
        return analysis

