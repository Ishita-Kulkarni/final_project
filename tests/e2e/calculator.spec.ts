import { test, expect, Page } from '@playwright/test';

/**
 * E2E Tests for Calculator UI with New Operations
 * Tests the calculator interface for power, modulus, square_root, and nth_root operations
 */

/**
 * Helper function to perform a calculation on the calculator UI
 */
async function performCalculation(page: Page, num1: string, num2: string, operation: string) {
  await page.fill('#num1', num1);
  if (operation !== 'square_root') {
    await page.fill('#num2', num2);
  }
  await page.click(`button[data-op="${operation}"]`);
  await page.click('.calculate-btn');
  
  // Wait for result to appear
  await expect(page.locator('.result.show')).toBeVisible({ timeout: 3000 });
}

/**
 * Helper function to get the result value
 */
async function getResult(page: Page): Promise<string> {
  return await page.locator('#resultValue').innerText();
}

/**
 * Helper function to check if error is displayed
 */
async function isError(page: Page): Promise<boolean> {
  const errorClass = await page.locator('#result').getAttribute('class');
  return errorClass?.includes('error') || false;
}

test.describe('Calculator UI - Basic Operations', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should load calculator page successfully', async ({ page }) => {
    await expect(page.locator('h1')).toContainText('FastAPI Calculator');
    await expect(page.locator('#num1')).toBeVisible();
    await expect(page.locator('#num2')).toBeVisible();
    await expect(page.locator('.calculate-btn')).toBeVisible();
  });

  test('should have all 8 operation buttons', async ({ page }) => {
    const operations = ['add', 'subtract', 'multiply', 'divide', 'power', 'modulus', 'square_root', 'nth_root'];
    
    for (const op of operations) {
      const button = page.locator(`button[data-op="${op}"]`);
      await expect(button).toBeVisible();
    }
  });
});

test.describe('Calculator UI - Power Operation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should calculate 2^3 = 8', async ({ page }) => {
    await performCalculation(page, '2', '3', 'power');
    const result = await getResult(page);
    expect(result).toBe('8');
  });

  test('should calculate 5^2 = 25 (square)', async ({ page }) => {
    await performCalculation(page, '5', '2', 'power');
    const result = await getResult(page);
    expect(result).toBe('25');
  });

  test('should calculate 10^0 = 1', async ({ page }) => {
    await performCalculation(page, '10', '0', 'power');
    const result = await getResult(page);
    expect(result).toBe('1');
  });

  test('should calculate 2^-1 = 0.5 (negative exponent)', async ({ page }) => {
    await performCalculation(page, '2', '-1', 'power');
    const result = await getResult(page);
    expect(result).toBe('0.5');
  });

  test('should display helper text for power operation', async ({ page }) => {
    await page.click('button[data-op="power"]');
    const helperText = await page.locator('#helper-text').innerText();
    expect(helperText).toContain('exponent');
  });
});

test.describe('Calculator UI - Modulus Operation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should calculate 10 % 3 = 1', async ({ page }) => {
    await performCalculation(page, '10', '3', 'modulus');
    const result = await getResult(page);
    expect(result).toBe('1');
  });

  test('should calculate 17 % 5 = 2', async ({ page }) => {
    await performCalculation(page, '17', '5', 'modulus');
    const result = await getResult(page);
    expect(result).toBe('2');
  });

  test('should calculate 20 % 4 = 0 (exact division)', async ({ page }) => {
    await performCalculation(page, '20', '4', 'modulus');
    const result = await getResult(page);
    expect(result).toBe('0');
  });

  test('should show error for modulus by zero', async ({ page }) => {
    await performCalculation(page, '10', '0', 'modulus');
    const error = await isError(page);
    expect(error).toBe(true);
    
    const errorText = await page.locator('#resultDetails').innerText();
    expect(errorText.toLowerCase()).toContain('modulus');
  });

  test('should display helper text for modulus operation', async ({ page }) => {
    await page.click('button[data-op="modulus"]');
    const helperText = await page.locator('#helper-text').innerText();
    expect(helperText).toContain('divisor');
  });
});

test.describe('Calculator UI - Square Root Operation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should calculate √16 = 4', async ({ page }) => {
    await performCalculation(page, '16', '', 'square_root');
    const result = await getResult(page);
    expect(result).toBe('4');
  });

  test('should calculate √9 = 3', async ({ page }) => {
    await performCalculation(page, '9', '', 'square_root');
    const result = await getResult(page);
    expect(result).toBe('3');
  });

  test('should calculate √0 = 0', async ({ page }) => {
    await performCalculation(page, '0', '', 'square_root');
    const result = await getResult(page);
    expect(result).toBe('0');
  });

  test('should calculate √2 ≈ 1.414', async ({ page }) => {
    await performCalculation(page, '2', '', 'square_root');
    const result = await getResult(page);
    const numResult = parseFloat(result);
    expect(numResult).toBeCloseTo(1.414213, 3);
  });

  test('should show error for square root of negative number', async ({ page }) => {
    await performCalculation(page, '-4', '', 'square_root');
    const error = await isError(page);
    expect(error).toBe(true);
    
    const errorText = await page.locator('#resultDetails').innerText();
    expect(errorText.toLowerCase()).toContain('negative');
  });

  test('should disable num2 input for square root', async ({ page }) => {
    await page.click('button[data-op="square_root"]');
    const num2Disabled = await page.locator('#num2').isDisabled();
    expect(num2Disabled).toBe(true);
  });

  test('should display helper text for square root operation', async ({ page }) => {
    await page.click('button[data-op="square_root"]');
    const helperText = await page.locator('#helper-text').innerText();
    expect(helperText).toContain('not needed');
  });
});

test.describe('Calculator UI - Nth Root Operation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should calculate 2√9 = 3 (square root)', async ({ page }) => {
    await performCalculation(page, '9', '2', 'nth_root');
    const result = await getResult(page);
    const numResult = parseFloat(result);
    expect(numResult).toBeCloseTo(3, 3);
  });

  test('should calculate 3√27 = 3 (cube root)', async ({ page }) => {
    await performCalculation(page, '27', '3', 'nth_root');
    const result = await getResult(page);
    const numResult = parseFloat(result);
    expect(numResult).toBeCloseTo(3, 3);
  });

  test('should calculate 4√16 = 2 (fourth root)', async ({ page }) => {
    await performCalculation(page, '16', '4', 'nth_root');
    const result = await getResult(page);
    const numResult = parseFloat(result);
    expect(numResult).toBeCloseTo(2, 3);
  });

  test('should calculate 3√-8 = -2 (odd root of negative)', async ({ page }) => {
    await performCalculation(page, '-8', '3', 'nth_root');
    const result = await getResult(page);
    const numResult = parseFloat(result);
    expect(numResult).toBeCloseTo(-2, 3);
  });

  test('should show error for even root of negative number', async ({ page }) => {
    await performCalculation(page, '-4', '2', 'nth_root');
    const error = await isError(page);
    expect(error).toBe(true);
    
    const errorText = await page.locator('#resultDetails').innerText();
    expect(errorText.toLowerCase()).toContain('even root');
  });

  test('should show error for zeroth root', async ({ page }) => {
    await performCalculation(page, '8', '0', 'nth_root');
    const error = await isError(page);
    expect(error).toBe(true);
    
    const errorText = await page.locator('#resultDetails').innerText();
    expect(errorText.toLowerCase()).toContain('zeroth root');
  });

  test('should display helper text for nth root operation', async ({ page }) => {
    await page.click('button[data-op="nth_root"]');
    const helperText = await page.locator('#helper-text').innerText();
    expect(helperText).toContain('root degree');
  });
});

test.describe('Calculator UI - Operation Switching', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should switch between operations correctly', async ({ page }) => {
    // Start with addition
    await page.fill('#num1', '10');
    await page.fill('#num2', '5');
    await page.click('button[data-op="add"]');
    await page.click('.calculate-btn');
    await expect(page.locator('.result.show')).toBeVisible();
    let result = await getResult(page);
    expect(result).toBe('15');

    // Switch to power
    await page.click('button[data-op="power"]');
    await page.click('.calculate-btn');
    await expect(page.locator('.result.show')).toBeVisible();
    result = await getResult(page);
    expect(result).toBe('100000'); // 10^5

    // Switch to modulus
    await page.click('button[data-op="modulus"]');
    await page.click('.calculate-btn');
    await expect(page.locator('.result.show')).toBeVisible();
    result = await getResult(page);
    expect(result).toBe('0'); // 10 % 5
  });

  test('should highlight active operation button', async ({ page }) => {
    const powerButton = page.locator('button[data-op="power"]');
    await powerButton.click();
    
    const buttonClass = await powerButton.getAttribute('class');
    expect(buttonClass).toContain('active');
  });
});

test.describe('Calculator UI - Decimal Numbers', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should handle decimal numbers in power operation', async ({ page }) => {
    await performCalculation(page, '4', '0.5', 'power');
    const result = await getResult(page);
    const numResult = parseFloat(result);
    expect(numResult).toBeCloseTo(2, 3);
  });

  test('should handle decimal numbers in modulus operation', async ({ page }) => {
    await performCalculation(page, '10.5', '3', 'modulus');
    const result = await getResult(page);
    const numResult = parseFloat(result);
    expect(numResult).toBeCloseTo(1.5, 3);
  });

  test('should handle decimal numbers in square root', async ({ page }) => {
    await performCalculation(page, '6.25', '', 'square_root');
    const result = await getResult(page);
    expect(result).toBe('2.5');
  });
});

test.describe('Calculator UI - Input Validation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should show error when num1 is empty', async ({ page }) => {
    await page.fill('#num1', '');
    await page.fill('#num2', '5');
    await page.click('button[data-op="power"]');
    await page.click('.calculate-btn');
    
    await expect(page.locator('.result.error')).toBeVisible();
  });

  test('should show error when num2 is empty (for binary operations)', async ({ page }) => {
    await page.fill('#num1', '10');
    await page.fill('#num2', '');
    await page.click('button[data-op="power"]');
    await page.click('.calculate-btn');
    
    await expect(page.locator('.result.error')).toBeVisible();
  });

  test('should not require num2 for square root', async ({ page }) => {
    await page.fill('#num1', '16');
    await page.click('button[data-op="square_root"]');
    await page.click('.calculate-btn');
    
    await expect(page.locator('.result.show')).toBeVisible();
    const result = await getResult(page);
    expect(result).toBe('4');
  });
});

test.describe('Calculator UI - Result Display', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should display result with proper formatting', async ({ page }) => {
    await performCalculation(page, '2', '10', 'power');
    await expect(page.locator('#resultValue')).toBeVisible();
    await expect(page.locator('#resultDetails')).toBeVisible();
    
    const details = await page.locator('#resultDetails').innerText();
    expect(details).toContain('2');
    expect(details).toContain('10');
  });

  test('should show calculation expression for standard operations', async ({ page }) => {
    await performCalculation(page, '10', '3', 'modulus');
    const details = await page.locator('#resultDetails').innerText();
    expect(details).toContain('%');
    expect(details).toContain('10');
    expect(details).toContain('3');
  });

  test('should show special notation for square root', async ({ page }) => {
    await performCalculation(page, '16', '', 'square_root');
    const details = await page.locator('#resultDetails').innerText();
    expect(details).toContain('√');
    expect(details).toContain('16');
  });
});
