-- ============================================
-- (D) UPDATE A RECORD
-- ============================================

UPDATE calculations
SET result = 6
WHERE id = 1;  -- Updating the first calculation result

-- Verify the update
SELECT * FROM calculations WHERE id = 1;
