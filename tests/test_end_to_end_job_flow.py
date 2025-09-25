import time
from pages.job_posting_page import JobPostingPage
from pages.screening_page import ScreeningPage
from pages.interview_page import InterviewPage

def test_end_to_end_job_flow(browser):
    # Step 1: Go to Job Posting page
    page = JobPostingPage(browser)
    browser.get("https://careers.hireskilldev.com/hireskill-ai/job/create/job-rounds?step=1")  # update URL

    # Step 2: Enter Job Role and Experience
    page.enter_job_role("Python Developer")
    page.enter_experience("2")
    page.click_next()

    # Step 3: Verify AI-generated JD
    time.sleep(3)  # wait for AI response
    jd_text = page.get_jd_text()
    assert "Python Developer" in jd_text

    # Step 4: Screening Questions
    screening = ScreeningPage(browser)
    time.sleep(3)
    screening_text = screening.get_screening_text()
    assert "question" in screening_text.lower()
    screening.click_next()

    # Step 5: Interview Topics
    interview = InterviewPage(browser)
    time.sleep(3)
    topics = interview.get_topics_text()
    assert "interview" in topics.lower()
