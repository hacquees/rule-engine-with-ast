// Create Rule Form Submission
document.getElementById('createRuleForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const ruleString = document.getElementById('createRuleString').value;

    fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule_string: ruleString }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('createRuleResult').textContent = `Created Rule AST: ${data.ast}`;
    })
    .catch((error) => {
        document.getElementById('createRuleResult').textContent = `Error: ${error}`;
    });
});

// Combine Rules Form Submission
document.getElementById('combineRulesForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const rules = document.getElementById('combineRulesStrings').value.trim().split('\n'); // Split by line

    fetch('/combine_rules', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rules: rules }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('combineRulesResult').textContent = `Combined Rule AST: ${data.combined_ast}`;
    })
    .catch((error) => {
        document.getElementById('combineRulesResult').textContent = `Error: ${error}`;
    });
});

// Evaluate Rule Form Submission
document.getElementById('evaluateRuleForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const ast = document.getElementById('evaluateRuleAST').value;
    const userData = JSON.parse(document.getElementById('evaluateUserData').value); // Ensure valid JSON input
    console.log(ast,userData);
    fetch('/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ast: ast, user_data: userData }), // Send both AST and user data
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('evaluateRuleResult').textContent = `Evaluation Result: ${data.result}`;
    })
    .catch((error) => {
        document.getElementById('evaluateRuleResult').textContent = `Error: ${error}`;
    });
});
