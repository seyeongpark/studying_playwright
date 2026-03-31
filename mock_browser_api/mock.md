# Playwright 모킹(Mocking) 가이드

Playwright에서의 **모킹(Mocking)**은 테스트 대상인 웹 애플리케이션이 의존하는 외부 요소(주로 API 서버)를 실제 데이터 대신 가짜 데이터로 대체하는 기술이다.

## 1. 정의 (Definition)
테스트 수행 시 실제 서버에 요청을 보내지 않고, 네트워크 레벨에서 요청을 가로채어(Intercept) 미리 정의된 응답을 돌려주는 행위이다. Playwright에서는 `page.route()` 메서드를 통해 이를 구현한다.

## 2. 목적 (Purpose)
* **테스트 속도 향상:** 서버의 비즈니스 로직이나 DB 조회를 거치지 않아 실행 시간이 단축된다.
* **결과 일관성 유지:** 외부 데이터가 변하더라도 테스트는 항상 동일한 가짜 데이터를 받으므로 결과가 안정적이다.
* **에러 케이스 검증:** 500 에러, 네트워크 지연, 권한 부족 등 실제 서버에서 발생시키기 어려운 상황을 강제로 재현할 수 있다.
* **개발 병목 해소:** 백엔드 API가 완성되지 않은 상태에서도 프론트엔드 기능 테스트가 가능하다.

## 3. 주요 쓰임새 및 코드 예시

### ① API 응답 모킹 (JSON 데이터 반환)
특정 API 호출을 가로채서 원하는 JSON 데이터를 반환하도록 설정한다.

```javascript
// 모든 /api/v1/users 요청을 가로채서 가짜 목록 반환
await page.route('**/api/v1/users', async route => {
  const json = [
    { id: 1, name: 'Test User 1' },
    { id: 2, name: 'Test User 2' }
  ];
  await route.fulfill({ json });
});
```

### ② HTTP 상태 코드 및 에러 테스트
서버 장애 상황을 가정하여 UI의 대응 로직을 확인한다.

```javascript
// API 호출 시 500 서버 에러를 강제로 반환
await page.route('**/api/data', async route => {
  await route.fulfill({
    status: 500,
    contentType: 'application/json',
    body: JSON.stringify({ error: 'Internal Server Error' })
  });
});
```

### ③ 리소스 로딩 차단
테스트와 무관한 리소스를 차단하여 속도를 최적화한다.

```javascript
// 이미지 파일(.png, .jpg 등) 로딩을 차단
await page.route('**/*.{png,jpg,jpeg}', route => route.abort());
```

## 4. 장단점 요약

| 구분 | 장점 | 단점 |
| :--- | :--- | :--- |
| **안정성** | 외부 환경 변화에 영향을 받지 않음 | 실제 서버 스펙 변경 시 모킹 데이터 업데이트 필요 |
| **효율성** | 테스트 실행 속도가 매우 빠름 | 실제 운영 환경의 데이터 흐름과 다를 수 있음 |
| **검증 범위** | 특수 에러 상황을 쉽게 재현 가능 | 과도한 모킹은 전체 시스템 통합 검증 능력을 저하시킴 |

## 5. 결론
Playwright의 모킹은 **네트워크 가로채기** 기능을 통해 구현되며, 주로 **테스트 실행 속도 최적화**와 **특수 상황(에러) 검증**을 위해 사용된다. 핵심 로직은 실제 API를 사용하되, 제어가 어렵거나 속도가 느린 부분에 선택적으로 적용하는 것이 권장된다.