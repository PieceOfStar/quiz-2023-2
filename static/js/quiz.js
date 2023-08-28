document.addEventListener('DOMContentLoaded', function() {
    const choices = document.querySelectorAll('a .quiz__c');

    // 각 요소에 클릭 이벤트 리스너를 추가합니다.
    choices.forEach(choice => {
        choice.addEventListener('click', function(event) {
            // 클릭 이벤트의 기본 동작을 중단합니다.
            event.preventDefault();

            // 먼저 모든 선택을 제거합니다.
            choices.forEach(c => c.classList.remove('selected'));
            
            // 클릭된 요소에 'selected' 클래스를 추가합니다.
            this.classList.add('selected');
            
            // 1초 딜레이 후 페이지 전환을 수행합니다.
            setTimeout(() => {
                window.location.href = this.parentElement.getAttribute('href'); // 다음 페이지로 이동
            }, 350);
        });
    });
});