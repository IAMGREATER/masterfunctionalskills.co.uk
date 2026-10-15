import os, glob
from build_all_curriculum_pages import transform_generic_topic, PRESERVED_FILES

TOPICS_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/topics"
PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

# Add perimeter to preserved so bespoke version is kept
PRESERVED_FILES.add("functional-skills-perimeter.html")

files = sorted(os.path.basename(f) for f in glob.glob(os.path.join(TOPICS_DIR, "*.html")))
print(f"Total topics to process: {len(files)}")
print(f"Preserved files (not overwritten): {PRESERVED_FILES}")

success = 0
skipped = 0
failed = []

for f in files:
    if f in PRESERVED_FILES:
        print(f"[PRESERVED] Skipping {f}")
        skipped += 1
        continue
    try:
        res = transform_generic_topic(f)
        if res:
            success += 1
        else:
            failed.append(f)
    except Exception as e:
        print(f"[ERROR] Failed on {f}: {e}")
        failed.append(f)

print("="*60)
print(f"Batch modernization complete!")
print(f"Successfully processed: {success}")
print(f"Preserved: {skipped}")
print(f"Failed: {len(failed)}")
if failed:
    print(f"Failed files: {failed}")
