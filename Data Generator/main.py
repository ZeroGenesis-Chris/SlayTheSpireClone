from DataGenerator import SlayTheSpireDataGenerator
import json
def main():
    generator = SlayTheSpireDataGenerator(num_players=5000)
    df = generator.generate_dataset()
    df.to_csv('slay_the_spire_analytics.csv', index=False)
    
    analysis = generator.analyze_dataset(df)
    
    with open('slay_the_spire_analysis.json', 'w') as f:
        json.dump({k: str(v) for k, v in analysis.items()}, f, indent=2)
    
    print("Slay the Spire dataset and analysis generated!")

if __name__ == "__main__":
    main()