**Pytest uchun test kodini quyidagicha yozing:**

```python
import pytest
from kompyuter import Kompyuter

def test_kompyuter_topadi():
    kompyuter = Kompyuter()
    assert kompyuter.topadi() == 42

def test_kompyuter_topadi_sana():
    kompyuter = Kompyuter()
    assert kompyuter.topadi(sana=10) == 42

def test_kompyuter_topadi_sana_limit():
    kompyuter = Kompyuter()
    assert kompyuter.topadi(sana=10, limit=100) == 42

def test_kompyuter_topadi_sana_limit_ishlatilmadi():
    kompyuter = Kompyuter()
    assert kompyuter.topadi(sana=10, limit=0) == 42

def test_kompyuter_topadi_sana_limit_ishlatilmadi_ishlatiladi():
    kompyuter = Kompyuter()
    assert kompyuter.topadi(sana=10, limit=42) == 42
```

**Jest uchun test kodini quyidagicha yozing:**

```javascript
import Kompyuter from './kompyuter';

describe('Kompyuter', () => {
  it('topadi', () => {
    const kompyuter = new Kompyuter();
    expect(kompyuter.topadi()).toBe(42);
  });

  it('topadi sana', () => {
    const kompyuter = new Kompyuter();
    expect(kompyuter.topadi(10)).toBe(42);
  });

  it('topadi sana limit', () => {
    const kompyuter = new Kompyuter();
    expect(kompyuter.topadi(10, 100)).toBe(42);
  });

  it('topadi sana limit ishlatilmadi', () => {
    const kompyuter = new Kompyuter();
    expect(kompyuter.topadi(10, 0)).toBe(42);
  });

  it('topadi sana limit ishlatilmadi ishlatiladi', () => {
    const kompyuter = new Kompyuter();
    expect(kompyuter.topadi(10, 42)).toBe(42);
  });
});
```
