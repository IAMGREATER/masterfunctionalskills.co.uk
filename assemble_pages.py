import re

with open('past-papers.html') as f:
    orig = f.read()

# Read the rendered cards
with open('/tmp/mfs_all_cards.html') as f:
    cards_html = f.read()

# 1. Update visible count default
orig = re.sub(r'Showing <span id="visibleCount">\d+</span>', 'Showing <span id="visibleCount">369</span>', orig)

# 2. Check CSS styles for .btn-paper-online, .btn-paper-video, etc.
if '.btn-paper-video' not in orig:
    video_css = """
    .btn-paper-video {
      background: #fdf2f8 !important;
      color: #be185d !important;
      border: 1px solid #fbcfe8 !important;
      font-weight: 700;
    }
    .btn-paper-video:hover {
      background: #fce7f3 !important;
    }
    """
    orig = orig.replace('.btn-paper-mock:hover {', video_css + '\n    .btn-paper-mock:hover {')

# 3. Find bounds for grid replacement
start_marker = '<div class="papers-grid view-list" id="papersGrid">'
end_marker = '<!-- NO RESULTS MESSAGE -->'

start_idx = orig.find(start_marker)
end_idx = orig.find(end_marker)

if start_idx == -1 or end_idx == -1:
    raise Exception("Could not find start or end markers for grid replacement")

before_grid = orig[:start_idx]

# Check if online simulator banner is already present
banner_html = """
    <!-- INTERACTIVE MOCK EXAM PORTALS BANNER -->
    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%); border: 1px solid #bbf7d0; border-radius: 14px; padding: 14px 20px; margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
      <div style="display: flex; align-items: center; gap: 14px;">
        <div style="width: 40px; height: 40px; border-radius: 10px; background: #16a34a; color: #ffffff; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;"><i class="fa-solid fa-laptop-code"></i></div>
        <div>
          <strong style="color: #14532d; font-size: 1rem; display: block; margin-bottom: 2px;">Interactive Online Mock Exams &amp; Simulators Available</strong>
          <span style="color: #166534; font-size: 0.88rem;">Official onscreen practice exams available for <strong>Open Awards (XAMS Platform)</strong> and <strong>Pearson Edexcel (Test Player Simulator)</strong>.</span>
        </div>
      </div>
      <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
        <button type="button" class="filter-chip" onclick="filterByBoardDirect('Open Awards')" style="background: #ffffff; border: 1px solid #86efac; color: #14532d; font-weight: 700; font-size: 0.84rem; padding: 7px 15px; border-radius: 20px; cursor: pointer; display: inline-flex; align-items: center; gap: 6px;">
          <img src="assets/img/boards/open-awards.png" alt="Open Awards" style="height: 18px; vertical-align: middle;"> Open Awards Online Tests
        </button>
        <a href="digital-functional-skills-mock-exam.html" class="filter-chip" style="background: #15803d; border: 1px solid #166534; color: #ffffff; font-weight: 700; font-size: 0.84rem; padding: 7px 15px; border-radius: 20px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
          <i class="fa-solid fa-desktop"></i> Pearson DFS Simulator
        </a>
      </div>
    </div>
"""

# Let's check what comes after end_marker
after_marker_idx = orig.find('<footer class="mfs-footer">')
if after_marker_idx == -1:
    raise Exception("Could not find footer tag")

middle_structure = f"""{banner_html}
    <div class="papers-grid view-list" id="papersGrid">
{cards_html}
    </div>

    <!-- NO RESULTS MESSAGE -->
    <div class="no-results" id="noResultsMsg" style="display: none;">
      <div style="font-size: 2.2rem; color: var(--text-muted); margin-bottom: 12px;"><i class="fa-regular fa-folder-open"></i></div>
      <h3 style="color: var(--navy); margin-bottom: 8px;">No past papers found</h3>
      <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 16px;">Try adjusting your keyword search or clear your filter selections.</p>
      <button class="btn-paper btn-paper-qp" onclick="resetAllFilters()" style="margin: 0 auto; display: inline-flex;">Clear Filters</button>
    </div>
  </main>

  """

footer_and_script = orig[after_marker_idx:]

# Improve JavaScript filtering logic
script_replacement = """  <script src="assets/js/mfs-core.js"></script>
  <script>
    let activeSubj = 'all';
    let activeLevel = 'all';
    let activeBoard = 'all';

    function setChip(btn, type) {
      const targetBtn = btn.closest('.filter-chip') || btn;
      const parent = targetBtn.parentElement;
      parent.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active', 'chip-accent'));
      targetBtn.classList.add('active');
      if (type === 'subj' && targetBtn.dataset.filter === 'all') {
        targetBtn.classList.add('chip-accent');
      }
      
      if (type === 'subj') {
        activeSubj = targetBtn.dataset.filter;
      } else if (type === 'level') {
        activeLevel = targetBtn.dataset.filter;
      } else if (type === 'board') {
        activeBoard = targetBtn.dataset.filter;
        
        // Smart filter: If user selects an Awarding Body, check if the current Subject filter has any cards for this board.
        // If not (e.g. Open Awards has no Digital Skills papers), auto-reset Subject to 'all' so cards appear immediately.
        if (activeBoard !== 'all' && activeSubj !== 'all') {
          const normBoard = activeBoard.toLowerCase().replace(/&amp;/g, '&').trim();
          const normSubj = activeSubj.toLowerCase().trim();
          const cards = document.querySelectorAll('#papersGrid .paper-card');
          const hasMatchingCard = Array.from(cards).some(card => {
            const b = (card.dataset.board || '').toLowerCase().replace(/&amp;/g, '&').trim();
            const s = (card.dataset.subj || '').toLowerCase().trim();
            return (b === normBoard || b.includes(normBoard) || normBoard.includes(b)) && s === normSubj;
          });
          if (!hasMatchingCard) {
            activeSubj = 'all';
            document.querySelectorAll('#subjChips .filter-chip').forEach((c, idx) => {
              c.classList.toggle('active', idx === 0);
              if (idx === 0) c.classList.add('chip-accent');
              else c.classList.remove('active', 'chip-accent');
            });
          }
        }
      }

      applyHubFilters();
    }

    function filterByBoardDirect(boardName) {
      const targetChip = Array.from(document.querySelectorAll('#boardChips .filter-chip')).find(c => {
        const f = (c.dataset.filter || '').toLowerCase().replace(/&amp;/g, '&').trim();
        return f === boardName.toLowerCase().replace(/&amp;/g, '&').trim();
      });
      if (targetChip) {
        setChip(targetChip, 'board');
        targetChip.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function resetAllFilters() {
      const searchInput = document.getElementById('hubSearch');
      if (searchInput) searchInput.value = '';
      activeSubj = 'all';
      activeLevel = 'all';
      activeBoard = 'all';

      document.querySelectorAll('#subjChips .filter-chip').forEach((c, idx) => {
        c.classList.toggle('active', idx === 0);
        if (idx === 0) c.classList.add('chip-accent');
        else c.classList.remove('active', 'chip-accent');
      });
      document.querySelectorAll('#levelChips .filter-chip').forEach((c, idx) => {
        c.classList.toggle('active', idx === 0);
        if (idx !== 0) c.classList.remove('active');
      });
      document.querySelectorAll('#boardChips .filter-chip').forEach((c, idx) => {
        c.classList.toggle('active', idx === 0);
        if (idx !== 0) c.classList.remove('active');
      });

      applyHubFilters();
    }

    // Layout View Switcher: List vs Tiles (Defaults to List as requested)
    let currentViewMode = localStorage.getItem('mfs_papers_view_mode') || 'list';

    function setViewMode(mode) {
      currentViewMode = mode;
      localStorage.setItem('mfs_papers_view_mode', mode);

      const grid = document.getElementById('papersGrid');
      const btnList = document.getElementById('btnViewList');
      const btnTiles = document.getElementById('btnViewTiles');

      if (!grid) return;

      if (mode === 'tiles') {
        grid.classList.remove('view-list');
        grid.classList.add('view-tiles');
        if (btnTiles) btnTiles.classList.add('active');
        if (btnList) btnList.classList.remove('active');
      } else {
        // Default to List
        grid.classList.remove('view-tiles');
        grid.classList.add('view-list');
        if (btnList) btnList.classList.add('active');
        if (btnTiles) btnTiles.classList.remove('active');
      }
    }

    function applyHubFilters() {
      const query = (document.getElementById('hubSearch')?.value || '').toLowerCase().trim();
      const cards = document.querySelectorAll('#papersGrid .paper-card');
      let visible = 0;

      const fSubj = (activeSubj || 'all').toLowerCase().trim();
      const fLevel = (activeLevel || 'all').toLowerCase().trim();
      const fBoard = (activeBoard || 'all').toLowerCase().replace(/&amp;/g, '&').trim();

      cards.forEach(card => {
        const b = (card.dataset.board || '').toLowerCase().replace(/&amp;/g, '&').trim();
        const s = (card.dataset.subj || '').toLowerCase().trim();
        const l = (card.dataset.level || '').toLowerCase().trim();
        const t = (card.dataset.title || '').toLowerCase().trim();

        const matchSubj = (fSubj === 'all' || s === fSubj);
        const matchLevel = (fLevel === 'all' || l === fLevel);
        const matchBoard = (fBoard === 'all' || b === fBoard || b.includes(fBoard) || fBoard.includes(b));
        const matchQuery = (!query || t.includes(query));

        if (matchSubj && matchLevel && matchBoard && matchQuery) {
          card.classList.remove('is-hidden');
          card.style.removeProperty('display');
          visible++;
        } else {
          card.classList.add('is-hidden');
          card.style.setProperty('display', 'none', 'important');
        }
      });

      const countEl = document.getElementById('visibleCount');
      if (countEl) countEl.textContent = visible;

      const noResEl = document.getElementById('noResultsMsg');
      if (noResEl) noResEl.style.display = (visible === 0) ? 'block' : 'none';
    }

    // Multi-parameter URL handler on page load
    window.addEventListener('DOMContentLoaded', () => {
      setViewMode(currentViewMode);

      const params = new URLSearchParams(window.location.search);
      const bParam = params.get('board');
      const sParam = params.get('subj');
      const lParam = params.get('level');

      if (bParam) {
        const cleanB = bParam.toLowerCase().replace(/\\+/g, ' ').replace(/&amp;/g, '&').trim();
        const targetChip = Array.from(document.querySelectorAll('#boardChips .filter-chip')).find(c => {
          const f = (c.dataset.filter || '').toLowerCase().replace(/&amp;/g, '&').trim();
          return f === cleanB || f.includes(cleanB) || cleanB.includes(f);
        });
        if (targetChip) {
          document.querySelectorAll('#boardChips .filter-chip').forEach(c => c.classList.remove('active'));
          targetChip.classList.add('active');
          activeBoard = targetChip.dataset.filter;
        }
      }
      if (sParam) {
        const cleanS = sParam.toLowerCase().replace(/\\+/g, ' ').trim();
        const targetChip = Array.from(document.querySelectorAll('#subjChips .filter-chip')).find(c => {
          const f = (c.dataset.filter || '').toLowerCase().trim();
          return f === cleanS || f.includes(cleanS) || cleanS.includes(f);
        });
        if (targetChip) {
          document.querySelectorAll('#subjChips .filter-chip').forEach(c => c.classList.remove('active', 'chip-accent'));
          targetChip.classList.add('active');
          activeSubj = targetChip.dataset.filter;
        }
      }
      if (lParam) {
        const cleanL = lParam.toLowerCase().replace(/\\+/g, ' ').trim();
        const targetChip = Array.from(document.querySelectorAll('#levelChips .filter-chip')).find(c => {
          const f = (c.dataset.filter || '').toLowerCase().trim();
          return f === cleanL || f.includes(cleanL) || cleanL.includes(f);
        });
        if (targetChip) {
          document.querySelectorAll('#levelChips .filter-chip').forEach(c => c.classList.remove('active'));
          targetChip.classList.add('active');
          activeLevel = targetChip.dataset.filter;
        }
      }
      applyHubFilters();
    });
  </script>
</body>
</html>
"""

# Replace the script at the bottom of footer_and_script
footer_only = footer_and_script[:footer_and_script.find('<script src="assets/js/mfs-core.js">')]
final_html = before_grid + middle_structure + footer_only + script_replacement

with open('past-papers.html', 'w') as f:
    f.write(final_html)

with open('functional-skills-past-papers.html', 'w') as f:
    f.write(final_html)

print("Successfully written updated past-papers.html and functional-skills-past-papers.html!")
