from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def solve_seating(students, rows, cols):
    """CSP Backtracking solver - no adjacent same branch"""
    seats = [[None for _ in range(cols)] for _ in range(rows)]
    
    if len(students) > rows * cols:
        return None
    
    def is_valid(r, c, student):
        branch = student['branch']
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if seats[nr][nc] and seats[nr][nc]['branch'] == branch:
                    return False
        return True
    
    def backtrack(remaining):
        if not remaining:
            return True
        for r in range(rows):
            for c in range(cols):
                if seats[r][c] is None:
                    for i, student in enumerate(remaining):
                        if is_valid(r, c, student):
                            seats[r][c] = student
                            if backtrack(remaining[:i] + remaining[i+1:]):
                                return True
                            seats[r][c] = None
                    return False
        return True
    
    sorted_students = sorted(students, key=lambda x: x['branch'])
    if backtrack(sorted_students):
        return seats
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    students = data['students']
    rows = data['rows']
    cols = data['cols']
    
    result = solve_seating(students, rows, cols)
    
    if result:
        return jsonify({'success': True, 'seats': result})
    return jsonify({'success': False, 'message': 'No valid arrangement found'})

if __name__ == '__main__':
    app.run(debug=True)