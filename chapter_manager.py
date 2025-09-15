#!/usr/bin/env python3
"""
Chapter Manager for "The Dream Walker" Novel
Automatically manages chapter files, master.md, and backup.txt
"""

import os
import shutil
from datetime import datetime
import re

class ChapterManager:
    def __init__(self, novel_title="The Dream Walker"):
        self.novel_title = novel_title
        self.chapters_dir = "chapters"
        self.master_file = "master.md"
        self.backup_file = f"{novel_title.lower().replace(' ', '_')}_backup.txt"
        
        # Ensure chapters directory exists
        os.makedirs(self.chapters_dir, exist_ok=True)
        
    def create_chapter_file(self, chapter_num, title, content=""):
        """Create a new chapter file with proper naming"""
        # Clean title for filename
        clean_title = re.sub(r'[^\w\s-]', '', title).strip()
        clean_title = re.sub(r'[-\s]+', '_', clean_title)
        
        filename = f"chapter_{chapter_num:02d}_{clean_title.lower()}.md"
        filepath = os.path.join(self.chapters_dir, filename)
        
        # Write chapter content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Chapter {chapter_num}: {title}\n\n")
            f.write(content)
        
        print(f"Created: {filepath}")
        return filepath
    
    def update_master_file(self):
        """Update master.md with all chapters"""
        master_content = f"# {self.novel_title}\n\n"
        master_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        master_content += "---\n\n"
        
        # Get all chapter files sorted by number
        chapter_files = []
        for filename in os.listdir(self.chapters_dir):
            if filename.startswith("chapter_") and filename.endswith(".md"):
                chapter_files.append(filename)
        
        chapter_files.sort()
        
        # Read and combine all chapters
        for filename in chapter_files:
            filepath = os.path.join(self.chapters_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                master_content += content + "\n\n---\n\n"
        
        # Write master file
        with open(self.master_file, 'w', encoding='utf-8') as f:
            f.write(master_content)
        
        print(f"Updated: {self.master_file}")
    
    def create_backup(self):
        """Create backup.txt file"""
        if os.path.exists(self.master_file):
            shutil.copy2(self.master_file, self.backup_file)
            print(f"Backup created: {self.backup_file}")
        else:
            print("No master file to backup")
    
    def add_chapter(self, chapter_num, title, content):
        """Add a new chapter and update all files"""
        self.create_chapter_file(chapter_num, title, content)
        self.update_master_file()
        self.create_backup()
        print(f"Chapter {chapter_num} added successfully!")
    
    def list_chapters(self):
        """List all existing chapters"""
        chapters = []
        for filename in os.listdir(self.chapters_dir):
            if filename.startswith("chapter_") and filename.endswith(".md"):
                chapters.append(filename)
        chapters.sort()
        
        print(f"\nExisting chapters in '{self.novel_title}':")
        for chapter in chapters:
            print(f"  - {chapter}")
        return chapters

def main():
    """Main function for command line usage"""
    manager = ChapterManager()
    
    if len(os.sys.argv) > 1:
        command = os.sys.argv[1]
        
        if command == "list":
            manager.list_chapters()
        elif command == "update":
            manager.update_master_file()
            manager.create_backup()
        elif command == "backup":
            manager.create_backup()
        else:
            print("Usage: python chapter_manager.py [list|update|backup]")
    else:
        print("Chapter Manager for 'The Dream Walker'")
        print("Usage: python chapter_manager.py [list|update|backup]")

if __name__ == "__main__":
    main()