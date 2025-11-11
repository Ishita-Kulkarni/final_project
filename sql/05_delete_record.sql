-- ============================================
-- (E) DELETE A RECORD
-- ============================================

DELETE FROM calculations
WHERE id = 2;  -- Deleting the second calculation

-- Verify the deletion
SELECT * FROM calculations;
