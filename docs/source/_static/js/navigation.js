// Navigation enhancement script
document.addEventListener('DOMContentLoaded', function() {
    
    // Add scroll indicator when navigation is scrollable
    const navSide = document.querySelector('.wy-nav-side');
    const navMenu = document.querySelector('.wy-menu-vertical');
    
    if (navSide && navMenu) {
        // Check if navigation is scrollable
        function checkScrollable() {
            if (navMenu.scrollHeight > navMenu.clientHeight) {
                navSide.classList.add('scrollable');
            } else {
                navSide.classList.remove('scrollable');
            }
        }
        
        // Initial check
        checkScrollable();
        
        // Check on window resize
        window.addEventListener('resize', checkScrollable);
        
        // Add smooth scroll behavior for long navigation
        navMenu.addEventListener('wheel', function(e) {
            if (e.deltaY !== 0) {
                e.preventDefault();
                navMenu.scrollTop += e.deltaY;
            }
        });
    }
    
    // Add click handlers for collapsible sections
    const toctreeItems = document.querySelectorAll('.wy-menu-vertical li.toctree-l1 > a');
    
    toctreeItems.forEach(function(item) {
        const hasChildren = item.nextElementSibling && item.nextElementSibling.tagName === 'UL';
        
        if (hasChildren) {
            item.addEventListener('click', function(e) {
                const parent = this.parentElement;
                const isExpanded = parent.classList.contains('expanded');
                
                // Toggle expanded state
                if (isExpanded) {
                    parent.classList.remove('expanded');
                } else {
                    parent.classList.add('expanded');
                }
                
                // Prevent default only if it's not a link to a page
                if (this.getAttribute('href') === '#') {
                    e.preventDefault();
                }
            });
        }
    });
    
    // Add keyboard navigation support
    document.addEventListener('keydown', function(e) {
        const currentItem = document.querySelector('.wy-menu-vertical li.current > a');
        
        if (currentItem) {
            const currentLi = currentItem.parentElement;
            let nextItem = null;
            
            switch(e.key) {
                case 'ArrowDown':
                    nextItem = currentLi.nextElementSibling;
                    if (nextItem && nextItem.querySelector('a')) {
                        nextItem.querySelector('a').focus();
                    }
                    break;
                case 'ArrowUp':
                    nextItem = currentLi.previousElementSibling;
                    if (nextItem && nextItem.querySelector('a')) {
                        nextItem.querySelector('a').focus();
                    }
                    break;
                case 'ArrowRight':
                    if (currentLi.classList.contains('toctree-l1')) {
                        currentLi.classList.add('expanded');
                    }
                    break;
                case 'ArrowLeft':
                    if (currentLi.classList.contains('toctree-l1')) {
                        currentLi.classList.remove('expanded');
                    }
                    break;
            }
        }
    });
    
    // Add search functionality for navigation
    const searchInput = document.querySelector('.wy-side-nav-search input');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const navItems = document.querySelectorAll('.wy-menu-vertical li');
            
            navItems.forEach(function(item) {
                const link = item.querySelector('a');
                if (link) {
                    const text = link.textContent.toLowerCase();
                    if (text.includes(searchTerm)) {
                        item.style.display = '';
                        if (searchTerm) {
                            item.classList.add('search-highlight');
                        } else {
                            item.classList.remove('search-highlight');
                        }
                    } else {
                        item.style.display = 'none';
                        item.classList.remove('search-highlight');
                    }
                }
            });
        });
    }
});
