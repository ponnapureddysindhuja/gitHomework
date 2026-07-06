# Test Cases - Amazon Home Page

Below are the test cases derived from the provided screenshot.

## TC_001 - Search bar visibility and functionality
- Description: Verify the search bar is visible and accepts input.
- Pre-conditions: User on Amazon home page.
- Steps:
  1. Locate the search bar.
  2. Enter "laptop".
  3. Press Enter or click search.
- Expected Result: Search results relevant to "laptop" are displayed.
- Priority: High
- Notes: Also verify autocomplete suggestions appear.

## TC_002 - Top banner / hero carousel display
- Description: Verify the main hero banner displays and carousel arrows work.
- Pre-conditions: User on Amazon home page.
- Steps:
  1. Observe the hero banner.
  2. Click right arrow.
  3. Click left arrow.
- Expected Result: Banner image changes on arrow click and rotation (if enabled) continues.
- Priority: Medium
- Notes: Check for banner title text visibility.

## TC_003 - Prime watch now link
- Description: Verify "Project Hail Mary - Watch Now" or Prime link navigates correctly.
- Pre-conditions: User on Amazon home page.
- Steps:
  1. Click the Prime/watch now area or link.
- Expected Result: User is taken to the Prime video landing or promo page.
- Priority: Low
- Notes: Link may open in a new tab.

## TC_004 - Top navigation menu links
- Description: Verify top nav sections (All, Amazon Haul, Best Sellers...) open correct category pages.
- Pre-conditions: User on Amazon home page.
- Steps:
  1. Click each top nav link (e.g., Best Sellers).
- Expected Result: Corresponding category page loads with relevant products.
- Priority: High
- Notes: Verify page title or breadcrumbs.

## TC_005 - Account & Lists link behavior
- Description: Verify "Account & Lists" opens signin or account menu.
- Pre-conditions: User not signed in.
- Steps:
  1. Click "Account & Lists".
- Expected Result: Sign-in page appears or account dropdown with sign-in option.
- Priority: High
- Notes: If signed in, account menu should show user name.

## TC_006 - Shopping basket/cart icon
- Description: Verify cart icon shows items and opens cart page.
- Pre-conditions: User on Amazon home page with/without items.
- Steps:
  1. Click cart icon.
- Expected Result: Cart page opens showing items or empty-cart message.
- Priority: High
- Notes: Verify cart count badge updates after adding/removing items.

## TC_007 - Top deals and product tiles visibility
- Description: Verify "Top deals" and product tiles visible and clickable.
- Pre-conditions: User on Amazon home page.
- Steps:
  1. Scroll to Top deals section.
  2. Click a product tile.
- Expected Result: Product detail page opens for clicked item.
- Priority: Medium
- Notes: Check price and discount label visibility.

## TC_008 - Language / location selector
- Description: Verify location code and language selector display and can be changed.
- Pre-conditions: User on Amazon home page.
- Steps:
  1. Click location/language area.
  2. Change language or location.
- Expected Result: Site language or delivery location updates accordingly.
- Priority: Low
- Notes: Some changes may reload the page.

## TC_009 - Footer links and legal info
- Description: Verify footer contains Help, Terms, Privacy links and they open.
- Pre-conditions: User on Amazon home page.
- Steps:
  1. Scroll to footer.
  2. Click Help/Terms/Privacy.
- Expected Result: Respective informational pages open.
- Priority: Low
- Notes: Verify links open in same or new tab per site behavior.

## TC_010 - Responsive layout check (desktop)
- Description: Verify the homepage layout adapts to desktop viewport correctly.
- Pre-conditions: Desktop browser at common widths.
- Steps:
  1. Resize browser to 1366x768 and 1920x1080.
  2. Refresh page.
- Expected Result: Layout maintains correct alignment; elements not overlapping.
- Priority: Medium
- Notes: Also test in mobile viewport separately.
