document.addEventListener('DOMContentLoaded', function() {
    const choices = document.querySelectorAll('a .quiz__c');

    // 각 요소에 클릭 이벤트 리스너를 추가합니다.
    choices.forEach(choice => {
        choice.addEventListener('click', function() {
            // 먼저 모든 선택을 제거합니다.
            choices.forEach(c => c.classList.remove('selected'));
            
            // 클릭된 요소에 'selected' 클래스를 추가합니다.
            this.classList.add('selected');
        });
    });
});