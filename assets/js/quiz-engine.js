// THANG Botanicals Strain Quiz Algorithm v2.0
// Matches user preferences against 25-strain database

class StrainQuiz {
  constructor() {
    this.strains = []; // Will be populated from _data via JSON
    this.currentStep = 0;
    this.userProfile = {
      speed: null,        // 'fast', 'moderate', 'slow', 'balanced'
      primaryGoal: null,  // 'energy', 'social', 'focus', 'pain', 'anxiety'
      experience: null,   // 'beginner', 'experienced'
      timeOfDay: null,    // 'morning', 'afternoon', 'evening', 'night'
      sedation: null      // 'none', 'mild', 'heavy'
    };
    this.results = [];
    
this.questions = [
  {
    id: 'experience',
    text: 'Experience Level',
    options: [
      { value: 'beginner', label: 'New Explorer', desc: 'First time or occasional use' },
      { value: 'experienced', label: 'Seasoned Connoisseur', desc: 'Regular, know my preferences' }
    ]
  },
  {
    id: 'timeOfDay',
    text: 'When do you need this?',
    options: [
      { value: 'morning', label: 'Morning', desc: 'Start the day' },
      { value: 'afternoon', label: 'Afternoon', desc: 'Mid-day boost or relief' },
      { value: 'evening', label: 'Evening', desc: 'Wind down after work' },
      { value: 'night', label: 'Late Night', desc: 'Sleep support or late social' }
    ]
  },
  {
    id: 'primaryGoal',
    text: 'Primary Intention',
    options: [
      { value: 'energy', label: 'Clean Energy', desc: 'Like coffee but smoother' },
      { value: 'social', label: 'Social Enhancement', desc: 'Talkative, euphoric, social' },
      { value: 'focus', label: 'Deep Focus', desc: 'Productivity, flow state' },
      { value: 'pain', label: 'Physical Relief', desc: 'Pain management, body comfort' },
      { value: 'anxiety', label: 'Anxiety Relief', desc: 'Calm mind, stress relief' }
    ]
  },
  {
    id: 'speed',
    text: 'Energy Preference',
    options: [
      { value: 'fast', label: 'Fast & Uplifting', desc: 'Motivating, get-things-done' },
      { value: 'balanced', label: 'Balanced & Smooth', desc: 'Middle ground, adaptable' },
      { value: 'slow', label: 'Slow & Mellow', desc: 'Relaxing, grounding' }
    ]
  },
  {
    id: 'sedation',
    text: 'Sedation Tolerance',
    options: [
      { value: 'none', label: 'None', desc: 'Need to stay sharp and active' },
      { value: 'mild', label: 'Mild', desc: 'Relaxed but functional' },
      { value: 'heavy', label: 'Heavy', desc: 'Couch-lock acceptable or desired' }
    ]
  }
];

  init(strainData) {
    this.strains = strainData;
    this.renderQuestion();
    this.attachEventListeners();
  }

  attachEventListeners() {
    document.addEventListener('click', (e) => {
      if (e.target.matches('.quiz-option')) {
        this.handleAnswer(e.target.dataset.value);
      }
      if (e.target.matches('#quiz-restart')) {
        this.restart();
      }
      if (e.target.matches('#quiz-close')) {
        this.close();
      }
    });
  }

  renderQuestion() {
    const container = document.getElementById('quiz-content');
    const q = this.questions[this.currentStep];
    const progress = ((this.currentStep / this.questions.length) * 100).toFixed(0);
    
    container.innerHTML = `
      <div class="quiz-progress">
        <div class="progress-bar" style="width: ${progress}%"></div>
        <span class="progress-text">${this.currentStep + 1} / ${this.questions.length}</span>
      </div>
      
      <h3>${q.text} <span class="japanese-subtitle">${q.subtitle}</span></h3>
      <div class="quiz-options">
        ${q.options.map(opt => `
          <button class="quiz-option holo-card strain-${this.getColorClass(opt.value)}" data-value="${opt.value}">
            <div class="option-label">${opt.label}</div>
            <div class="option-desc">${opt.desc}</div>
          </button>
        `).join('')}
      </div>
    `;
  }

  getColorClass(value) {
    // Assign visual colors to options
    const map = {
      'fast': 'white', 'slow': 'red', 'balanced': 'yellow',
      'energy': 'white', 'social': 'green', 'focus': 'white', 'pain': 'red', 'anxiety': 'yellow',
      'morning': 'white', 'afternoon': 'green', 'evening': 'yellow', 'night': 'red'
    };
    return map[value] || 'green';
  }

  handleAnswer(value) {
    const currentQ = this.questions[this.currentStep];
    this.userProfile[currentQ.id] = value;
    
    if (this.currentStep < this.questions.length - 1) {
      this.currentStep++;
      this.renderQuestion();
    } else {
      this.calculateResults();
    }
  }

  calculateResults() {
    const scoredStrains = this.strains.map(strain => {
      let score = 0;
      let maxScore = 0;
      
      // Experience match (required)
      if (this.userProfile.experience === 'beginner' && strain.beginner) {
        score += 10;
      } else if (this.userProfile.experience === 'experienced' && !strain.beginner) {
        score += 10;
      } else if (this.userProfile.experience === 'experienced' && strain.beginner) {
        score += 5; // Experienced can use beginner strains
      }
      maxScore += 10;
      
      // Time of day match (high priority)
      if (strain.time_of_day.includes(this.userProfile.timeOfDay)) {
        score += 15;
      } else if (strain.time_of_day.includes('anytime')) {
        score += 10;
      }
      maxScore += 15;
      
      // Speed match (high priority)
      if (strain.speed === this.userProfile.speed) {
        score += 15;
      } else if (this.userProfile.speed === 'balanced' && (strain.speed === 'moderate')) {
        score += 10;
      }
      maxScore += 15;
      
      // Primary goal match (highest priority)
      switch(this.userProfile.primaryGoal) {
        case 'energy':
          score += (strain.energy / 10) * 20;
          break;
        case 'social':
          score += (strain.social / 10) * 20;
          break;
        case 'focus':
          score += (strain.focus / 10) * 20;
          break;
        case 'pain':
          score += (strain.pain / 10) * 20;
          break;
        case 'anxiety':
          score += (strain.anxiety / 10) * 20;
          break;
      }
      maxScore += 20;
      
      // Sedation preference
      if (this.userProfile.sedation === 'none' && strain.speed !== 'slow') score += 10;
      else if (this.userProfile.sedation === 'heavy' && strain.speed === 'slow') score += 10;
      else if (this.userProfile.sedation === 'mild') score += 5;
      maxScore += 10;
      
      // Limited edition bonus (rarity appeal)
      if (strain.limited) score += 2;
      
      const percentage = (score / maxScore) * 100;
      
      return {
        ...strain,
        matchScore: percentage.toFixed(1),
        matchReason: this.getMatchReason(strain)
      };
    });
    
    // Sort by score, filter out < 40% matches
    this.results = scoredStrains
      .filter(s => parseFloat(s.matchScore) > 40)
      .sort((a, b) => b.matchScore - a.matchScore)
      .slice(0, 3); // Top 3
      
    this.renderResults();
  }

  getMatchReason(strain) {
    const reasons = [];
    if (strain.time_of_day.includes(this.userProfile.timeOfDay)) {
      reasons.push(`Perfect for ${this.userProfile.timeOfDay}`);
    }
    if (this.userProfile.primaryGoal === 'energy' && strain.energy > 7) {
      reasons.push('High energy');
    }
    if (this.userProfile.primaryGoal === 'anxiety' && strain.anxiety > 7) {
      reasons.push('Anxiety relief');
    }
    if (strain.limited) {
      reasons.push('Limited edition');
    }
    return reasons.slice(0, 2).join(' • ');
  }

  renderResults() {
    const container = document.getElementById('quiz-content');
    
    container.innerHTML = `
      <h3>Your Recommendations <span class="japanese-subtitle">推奨事項</span></h3>
      <div class="results-container">
        ${this.results.map((strain, index) => `
          <div class="result-card holo-card strain-${strain.color} ${index === 0 ? 'top-match' : ''}">
            ${strain.limited ? '<span class="limited-badge">Limited</span>' : ''}
            <div class="match-percentage">${strain.matchScore}% Match</div>
            <h4>${strain.name}</h4>
            <div class="match-reason">${strain.matchReason}</div>
            <p>${strain.description}</p>
            <div class="strain-tags">
              ${strain.tags.slice(0, 3).map(tag => `<span class="tag">${tag}</span>`).join('')}
            </div>
            ${index === 0 ? '<div class="best-match-label">Best Match</div>' : ''}
          </div>
        `).join('')}
      </div>
      <div class="quiz-actions">
        <button id="quiz-restart" class="btn-gold">Retake Quiz</button>
        <button id="quiz-close" class="btn-gold">Browse Catalog</button>
      </div>
    `;
  }

  restart() {
    this.currentStep = 0;
    this.userProfile = {};
    this.results = [];
    this.renderQuestion();
  }

  close() {
    document.getElementById('quiz-modal').classList.remove('active');
    document.body.style.overflow = 'auto';
  }

  open() {
    document.getElementById('quiz-modal').classList.add('active');
    document.body.style.overflow = 'hidden';
    this.restart();
  }
}

// Export for global use
window.StrainQuiz = StrainQuiz;