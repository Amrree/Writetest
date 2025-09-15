#!/usr/bin/env python3
"""
Chapter Templates for "The Dream Walker"
Creates all 46 chapter files with proper naming
"""

from chapter_manager import ChapterManager

def create_all_chapter_templates():
    """Create all 46 chapter templates based on dream_walker_chapters.md"""
    
    manager = ChapterManager()
    
    # Chapter titles and brief descriptions
    chapters = [
        # ACT I: SETUP (Chapters 1-12)
        ("The First Dream", "Eli accidentally enters Mrs. Patterson's nightmare"),
        ("The Glowing Figure", "Eli encounters Nova in the dream realm"),
        ("Insomnia's Gift", "Eli realizes he can dream-walk"),
        ("The Dream Master", "Eli meets his mentor"),
        ("Training Begins", "Eli learns dream-walking basics"),
        ("The Nightmare King", "First encounter with the antagonist"),
        ("Maya's Secret", "Eli's sister reveals her own abilities"),
        ("The Tower Beckons", "Eli's recurring dream intensifies"),
        ("Dream Creatures", "Eli encounters shadow-wraiths and dream-spiders"),
        ("The First Quest", "Eli's first mission in the dream realm"),
        ("Nova's Past", "Eli learns about Nova's tragic history"),
        ("The Betrayal Setup", "Maya begins her secret alliance"),
        
        # ACT II: CONFRONTATION (Chapters 13-35)
        ("The Deep Dreams", "Eli ventures into complex symbolic dreams"),
        ("Nightmare Depths", "Eli explores the darkest dream layers"),
        ("The Tower's Call", "Eli is drawn toward the mysterious tower"),
        ("Dream Master's Warning", "Eli receives ominous guidance"),
        ("Maya's Alliance", "Maya secretly joins the Nightmare King"),
        ("The Dream Realm War", "Conflict escalates in the dream world"),
        ("Nova's Sacrifice", "Nova makes a dangerous choice"),
        ("Eli's Power Grows", "Eli's abilities strengthen"),
        ("The Tower's Secrets", "Eli discovers the tower's true nature"),
        ("Maya's Betrayal", "Maya's true allegiance is revealed"),
        ("The Nightmare King's Plan", "The antagonist's scheme unfolds"),
        ("Dream Creatures Attack", "Eli faces dangerous dream entities"),
        ("The Dream Master's Fall", "Eli's mentor is captured"),
        ("Eli's Descent", "Eli falls into despair"),
        ("Nova's Rescue Mission", "Nova attempts to save Eli"),
        ("The Tower's Heart", "Eli reaches the tower's core"),
        ("Maya's Regret", "Maya begins to question her choices"),
        ("The Nightmare King's Victory", "The antagonist seems to win"),
        ("Eli's Awakening", "Eli finds inner strength"),
        ("The Dream Realm's Hope", "Eli rallies dream-walkers"),
        ("Maya's Redemption", "Maya chooses to help Eli"),
        ("The Final Battle Begins", "Eli confronts the Nightmare King"),
        
        # ACT III: RESOLUTION (Chapters 36-46)
        ("The Tower's Fall", "Eli destroys the nightmare tower"),
        ("The Nightmare King's Defeat", "The antagonist is vanquished"),
        ("Dream Master's Return", "Eli's mentor is freed"),
        ("Maya's Apology", "Maya seeks forgiveness"),
        ("The Dream Realm's Healing", "The dream world begins to recover"),
        ("Eli's New Purpose", "Eli embraces his role as dream-walker"),
        ("Nova's Choice", "Nova decides her future"),
        ("The New Order", "Eli establishes peace in the dream realm"),
        ("Maya's New Path", "Maya finds redemption"),
        ("The Dream Walker's Legacy", "Eli's story becomes legend"),
        ("Epilogue: Sweet Dreams", "The story concludes with hope"),
        ("Afterword: The Dream Walker's Code", "Eli's final thoughts and legacy")
    ]
    
    print("Creating chapter templates...")
    
    for i, (title, description) in enumerate(chapters, 1):
        # Create empty chapter file
        content = f"*{description}*\n\n[Chapter content will be written here]"
        manager.create_chapter_file(i, title, content)
    
    # Update master file and create backup
    manager.update_master_file()
    manager.create_backup()
    
    print(f"\nCreated {len(chapters)} chapter templates!")
    print("Files created:")
    print("- Individual chapter files in 'chapters/' directory")
    print("- master.md (complete novel)")
    print("- the_dream_walker_backup.txt (backup)")

if __name__ == "__main__":
    create_all_chapter_templates()