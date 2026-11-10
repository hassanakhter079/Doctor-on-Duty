# -*- coding: utf-8 -*-
"""
Build Doctor on Duty Chapter 17 (General Surgery) Master Single Page Application
Generates /root/doctor-on-duty/index.html
"""
import sys, os, json
sys.path.append('/root/doctor-on-duty')

from data.mod1_acute_abdomen import TOPICS as T1
from data.mod2_hpb import TOPICS as T2
from data.mod3_colorectal import TOPICS as T3
from data.mod4_peritonitis import TOPICS as T4
from data.mod5_wounds import TOPICS as T5
from data.mod6_soft_tissue import TOPICS as T6
from data.mod7_hand_nail import TOPICS as T7

ALL_TOPICS = T1 + T2 + T3 + T4 + T5 + T6 + T7
# Sort strictly by topic number
ALL_TOPICS.sort(key=lambda x: x["num"])

print(f"Total verified topics loaded: {len(ALL_TOPICS)}")
assert len(ALL_TOPICS) == 29, f"Expected 29 topics, got {len(ALL_TOPICS)}"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Doctor on Duty | Chapter 17: General Surgery (29 Topics)</title>
  
  <!-- Universal HTML Cloud Sync -->
  <script src="https://hassanakhter079.github.io/After-Salah-Zikr/cloud-sync.js" data-app="doctor-on-duty"></script>

  <!-- Typography & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    :root {
      /* Clean Slate Clinical Palette */
      --bg-base: #f7f9fc;
      --bg-surface: #ffffff;
      --bg-surface-2: #f1f4f9;
      --bg-sidebar: #0f172a;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-light: #94a3b8;
      --border: #e2e8f0;
      --border-dark: #334155;

      /* Primary Accents */
      --teal-primary: #0d9488;
      --teal-hover: #0f766e;
      --teal-pale: #ccfbf1;
      --blue-accent: #2563eb;
      --blue-pale: #dbeafe;
      --amber-accent: #d97706;
      --amber-pale: #fef3c7;
      --rose-accent: #e11d48;
      --rose-pale: #ffe4e6;
      --purple-accent: #7c3aed;
      --purple-pale: #ede9fe;
      --emerald-accent: #059669;
      --emerald-pale: #d1fae5;

      /* Shadows & Radii */
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.03);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      
      --sidebar-width: 320px;
      --header-height: 64px;
    }

    [data-theme="dark"] {
      --bg-base: #090d16;
      --bg-surface: #111827;
      --bg-surface-2: #1e293b;
      --bg-sidebar: #0b1120;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-light: #64748b;
      --border: #1e293b;
      --border-dark: #334155;

      --teal-primary: #14b8a6;
      --teal-hover: #2dd4bf;
      --teal-pale: rgba(20, 184, 166, 0.15);
      --blue-accent: #3b82f6;
      --blue-pale: rgba(59, 130, 246, 0.15);
      --amber-accent: #f59e0b;
      --amber-pale: rgba(245, 158, 11, 0.15);
      --rose-accent: #f43f5e;
      --rose-pale: rgba(244, 63, 94, 0.15);
      --purple-accent: #8b5cf6;
      --purple-pale: rgba(139, 92, 246, 0.15);
      --emerald-accent: #10b981;
      --emerald-pale: rgba(16, 185, 129, 0.15);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    /* ── APP LAYOUT ── */
    .app-container {
      display: flex;
      min-height: 100vh;
    }

    /* ── SIDEBAR NAVIGATION ── */
    .sidebar {
      width: var(--sidebar-width);
      background-color: var(--bg-sidebar);
      color: #f8fafc;
      height: 100vh;
      position: sticky;
      top: 0;
      display: flex;
      flex-direction: column;
      border-right: 1px solid var(--border-dark);
      z-index: 100;
      transition: transform 0.3s ease;
    }

    .sidebar-header {
      padding: 18px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .app-logo {
      width: 38px;
      height: 38px;
      background: linear-gradient(135deg, var(--teal-primary), #0284c7);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      color: #fff;
      box-shadow: 0 4px 10px rgba(13, 148, 136, 0.35);
    }

    .app-title-group h1 {
      font-size: 15px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
      line-height: 1.2;
    }
    .app-title-group p {
      font-size: 11px;
      color: #94a3b8;
      font-weight: 500;
    }

    .sidebar-system-selector {
      padding: 12px 16px;
      background: rgba(255, 255, 255, 0.03);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .system-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(13, 148, 136, 0.25);
      border: 1px solid var(--teal-primary);
      color: #2dd4bf;
      padding: 5px 10px;
      border-radius: var(--radius-full);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .sidebar-search-box {
      padding: 12px 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      position: relative;
    }

    .sidebar-search-box input {
      width: 100%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-md);
      padding: 9px 12px 9px 34px;
      font-size: 12px;
      color: #ffffff;
      outline: none;
      transition: all 0.2s ease;
    }
    .sidebar-search-box input:focus {
      background: rgba(255, 255, 255, 0.1);
      border-color: var(--teal-primary);
    }
    .sidebar-search-box i {
      position: absolute;
      left: 28px;
      top: 50%;
      transform: translateY(-50%);
      color: #94a3b8;
      font-size: 12px;
    }

    .sidebar-nav {
      flex: 1;
      overflow-y: auto;
      padding: 12px 8px;
    }

    .sidebar-nav::-webkit-scrollbar { width: 5px; }
    .sidebar-nav::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.15); border-radius: 4px; }

    .nav-group-title {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      padding: 10px 12px 4px;
    }

    .nav-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: var(--radius-md);
      color: #cbd5e1;
      text-decoration: none;
      font-size: 12px;
      font-weight: 500;
      transition: all 0.15s ease;
      cursor: pointer;
      position: relative;
    }
    .nav-item:hover {
      background: rgba(255, 255, 255, 0.06);
      color: #ffffff;
    }
    .nav-item.active {
      background: linear-gradient(90deg, rgba(13, 148, 136, 0.3), rgba(13, 148, 136, 0.05));
      color: #2dd4bf;
      border-left: 3px solid var(--teal-primary);
    }
    .nav-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      color: #94a3b8;
      min-width: 20px;
    }
    .nav-title {
      flex: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .nav-star {
      font-size: 11px;
      color: rgba(255, 255, 255, 0.2);
      transition: color 0.15s;
    }
    .nav-star.starred {
      color: #f59e0b;
    }

    /* ── MAIN CONTENT AREA ── */
    .main-wrapper {
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
    }

    /* ── TOP HEADER / CONTROLS ── */
    .top-header {
      height: var(--header-height);
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      position: sticky;
      top: 0;
      z-index: 90;
      box-shadow: var(--shadow-sm);
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .mobile-menu-btn {
      display: none;
      background: transparent;
      border: none;
      color: var(--text-main);
      font-size: 18px;
      cursor: pointer;
    }

    .header-meta h2 {
      font-size: 16px;
      font-weight: 800;
      letter-spacing: -0.01em;
    }
    .header-meta span {
      font-size: 11px;
      color: var(--text-muted);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 14px;
      border-radius: var(--radius-md);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.15s ease;
    }
    .btn-secondary {
      background: var(--bg-surface-2);
      color: var(--text-main);
      border-color: var(--border);
    }
    .btn-secondary:hover {
      background: var(--border);
    }
    .btn-teal {
      background: var(--teal-primary);
      color: #ffffff;
    }
    .btn-teal:hover {
      background: var(--teal-hover);
    }

    /* ── CATEGORY PILL FILTER BAR ── */
    .filter-bar {
      padding: 12px 24px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      white-space: nowrap;
    }
    .filter-bar::-webkit-scrollbar { height: 4px; }
    .filter-bar::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

    .filter-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      background: var(--bg-surface-2);
      border: 1px solid var(--border);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .filter-pill:hover {
      background: var(--border);
      color: var(--text-main);
    }
    .filter-pill.active {
      background: var(--teal-primary);
      border-color: var(--teal-primary);
      color: #ffffff;
    }
    .filter-pill .pill-count {
      font-size: 10px;
      background: rgba(0, 0, 0, 0.12);
      padding: 1px 6px;
      border-radius: var(--radius-full);
    }
    .filter-pill.active .pill-count {
      background: rgba(255, 255, 255, 0.25);
    }

    /* ── CONTENT CONTAINER ── */
    .content-container {
      padding: 24px;
      max-width: 1180px;
      margin: 0 auto;
      width: 100%;
    }

    /* ── BANNER HERO ── */
    .system-hero {
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      padding: 28px;
      border-radius: var(--radius-lg);
      margin-bottom: 24px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }
    .system-hero::after {
      content: '';
      position: absolute;
      right: -20px;
      bottom: -20px;
      width: 220px;
      height: 220px;
      background: radial-gradient(circle, rgba(13, 148, 136, 0.3) 0%, transparent 70%);
      border-radius: 50%;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(13, 148, 136, 0.3);
      border: 1px solid var(--teal-primary);
      color: #2dd4bf;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 11px;
      font-weight: 700;
      margin-bottom: 10px;
    }
    .system-hero h2 {
      font-family: 'Fraunces', serif;
      font-size: 26px;
      font-weight: 700;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }
    .system-hero p {
      color: #cbd5e1;
      font-size: 13px;
      max-width: 760px;
      line-height: 1.5;
    }
    .hero-meta {
      display: flex;
      gap: 20px;
      margin-top: 16px;
      font-size: 12px;
      color: #94a3b8;
    }
    .hero-meta span {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .hero-meta strong {
      color: #f8fafc;
    }

    /* ── TOPIC CARDS ── */
    .topic-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .topic-card:hover {
      border-color: #cbd5e1;
      box-shadow: var(--shadow-md);
    }
    .topic-card.starred-card {
      border-left: 4px solid var(--amber-accent);
    }

    .card-header {
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
      background: var(--bg-surface);
      transition: background 0.15s ease;
    }
    .card-header:hover {
      background: var(--bg-surface-2);
    }

    .card-header-left {
      display: flex;
      align-items: center;
      gap: 14px;
      min-width: 0;
    }

    .topic-circle {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-md);
      background: var(--teal-pale);
      color: var(--teal-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 15px;
      font-weight: 700;
      flex-shrink: 0;
    }

    .topic-titles h3 {
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .topic-badges {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: 4px;
      flex-wrap: wrap;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-teal { background: var(--teal-pale); color: var(--teal-primary); }
    .badge-blue { background: var(--blue-pale); color: var(--blue-accent); }
    .badge-amber { background: var(--amber-pale); color: var(--amber-accent); }
    .badge-danger { background: var(--rose-pale); color: var(--rose-accent); }
    .badge-purple { background: var(--purple-pale); color: var(--purple-accent); }
    .badge-page { background: var(--bg-surface-2); color: var(--text-muted); border: 1px solid var(--border); font-family: 'JetBrains Mono', monospace; }

    .card-header-right {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }

    .star-btn {
      background: transparent;
      border: none;
      color: var(--text-light);
      font-size: 16px;
      cursor: pointer;
      padding: 4px;
      transition: color 0.15s;
    }
    .star-btn:hover, .star-btn.active {
      color: var(--amber-accent);
    }

    .expand-icon {
      font-size: 14px;
      color: var(--text-muted);
      transition: transform 0.25s ease;
    }
    .topic-card.open .expand-icon {
      transform: rotate(180deg);
    }

    .card-body {
      display: none;
      padding: 20px 24px 28px;
      border-top: 1px solid var(--border);
      background: var(--bg-surface);
    }
    .topic-card.open .card-body {
      display: block;
    }

    .topic-summary-box {
      background: var(--bg-surface-2);
      border-left: 3px solid var(--teal-primary);
      padding: 12px 16px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      font-size: 13px;
      color: var(--text-main);
      margin-bottom: 20px;
      font-weight: 500;
    }

    /* ── CLINICAL STYLING WITHIN TOPICS ── */
    .clinical-section h4 {
      font-size: 14px;
      font-weight: 800;
      color: var(--text-main);
      margin: 20px 0 10px;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .clinical-section h4:first-child { margin-top: 0; }

    .lead-text {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }

    .styled-list {
      list-style: none;
      padding-left: 0;
      margin-bottom: 14px;
    }
    .styled-list > li {
      position: relative;
      padding-left: 20px;
      margin-bottom: 8px;
      font-size: 13px;
    }
    .styled-list > li::before {
      content: '•';
      position: absolute;
      left: 6px;
      color: var(--teal-primary);
      font-weight: bold;
      font-size: 16px;
      line-height: 1;
      top: 0;
    }

    .sub-list {
      list-style: none;
      padding-left: 16px;
      margin-top: 6px;
    }
    .sub-list > li {
      position: relative;
      padding-left: 14px;
      margin-bottom: 4px;
      font-size: 12.5px;
      color: var(--text-muted);
    }
    .sub-list > li::before {
      content: '–';
      position: absolute;
      left: 0;
      color: var(--text-light);
    }

    .compact-list {
      list-style: none;
      padding-left: 0;
      font-size: 12px;
    }
    .compact-list li {
      margin-bottom: 3px;
      position: relative;
      padding-left: 12px;
    }
    .compact-list li::before {
      content: '›';
      position: absolute;
      left: 0;
      color: var(--teal-primary);
      font-weight: bold;
    }

    /* ── TABLES ── */
    .table-responsive {
      overflow-x: auto;
      margin: 14px 0 20px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
    }
    .med-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
      text-align: left;
    }
    .med-table th {
      background: var(--bg-surface-2);
      color: var(--text-main);
      padding: 10px 14px;
      font-weight: 700;
      border-bottom: 1px solid var(--border);
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.04em;
    }
    .med-table td {
      padding: 10px 14px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
      color: var(--text-main);
    }
    .med-table tr:last-child td { border-bottom: none; }
    .med-table tr:hover td { background: rgba(0, 0, 0, 0.015); }

    /* ── PRESCRIPTION & CALLOUT BOXES ── */
    .rx-box {
      background: var(--bg-surface-2);
      border: 1px solid #0d948840;
      border-radius: var(--radius-md);
      margin: 16px 0 20px;
      overflow: hidden;
    }
    .rx-header {
      background: linear-gradient(90deg, #0d9488, #0f766e);
      color: #ffffff;
      padding: 9px 16px;
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .rx-icon {
      font-family: 'Fraunces', serif;
      font-style: italic;
      font-size: 16px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.2);
      padding: 1px 8px;
      border-radius: 4px;
    }
    .rx-body {
      padding: 16px 20px;
      font-size: 13px;
    }

    .rx-ordered-list {
      padding-left: 20px;
      margin: 0;
    }
    .rx-ordered-list > li {
      margin-bottom: 12px;
      line-height: 1.5;
    }
    .rx-ordered-list > li:last-child { margin-bottom: 0; }

    .drug-name {
      font-weight: 700;
      color: var(--teal-primary);
    }
    .brand {
      font-weight: 700;
      color: var(--purple-accent);
      background: var(--purple-pale);
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 11.5px;
    }

    .callout {
      padding: 14px 18px;
      border-radius: var(--radius-md);
      margin: 16px 0;
      font-size: 12.5px;
      border-left: 4px solid;
    }
    .callout-info { background: var(--teal-pale); border-color: var(--teal-primary); color: var(--text-main); }
    .callout-danger { background: var(--rose-pale); border-color: var(--rose-accent); color: var(--text-main); }
    .callout-warning { background: var(--amber-pale); border-color: var(--amber-accent); color: var(--text-main); }

    /* ── PILL CLOUD & SUB-GRIDS ── */
    .pill-cloud {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 12px 0 16px;
    }
    .pill-item {
      background: var(--bg-surface-2);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: var(--radius-md);
      font-size: 12px;
      color: var(--text-main);
    }

    .cards-subgrid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
      margin: 14px 0 18px;
    }
    .subcard {
      background: var(--bg-surface-2);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      font-size: 12.5px;
    }
    .subcard-header {
      font-weight: 700;
      font-size: 13px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .primary-header { color: var(--teal-primary); }
    .warning-header { color: var(--amber-accent); }
    .danger-header { color: var(--rose-accent); }
    .info-header { color: var(--blue-accent); }
    .diag-tags {
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px dashed var(--border);
      font-size: 11.5px;
      color: var(--text-muted);
    }

    .steps-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 10px;
      margin: 12px 0 16px;
    }
    .step-card {
      background: var(--bg-surface-2);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 10px 12px;
      font-size: 12px;
    }
    .step-num {
      display: inline-block;
      width: 20px;
      height: 20px;
      background: var(--teal-primary);
      color: #fff;
      border-radius: 50%;
      text-align: center;
      line-height: 20px;
      font-size: 10px;
      font-weight: 700;
      margin-right: 6px;
    }

    .row-2col {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 20px;
      margin: 14px 0;
    }
    @media (max-width: 900px) {
      .row-2col { grid-template-columns: 1fr; }
    }

    /* ── INTERACTIVE CALCULATOR BOX ── */
    .calc-box {
      background: var(--bg-surface-2);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 16px;
    }
    .calc-box h4 {
      margin: 0 0 4px 0;
      font-size: 14px;
      color: var(--text-main);
    }
    .calc-sub {
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }
    .calc-checks {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .calc-label {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      cursor: pointer;
      padding: 5px 8px;
      border-radius: var(--radius-sm);
      transition: background 0.15s;
    }
    .calc-label:hover {
      background: rgba(0, 0, 0, 0.03);
    }
    .calc-label input[type="checkbox"] {
      width: 15px;
      height: 15px;
      accent-color: var(--teal-primary);
    }
    .calc-result {
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px solid var(--border);
    }
    .score-display {
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .score-badge {
      background: var(--teal-primary);
      color: #fff;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
    }
    .interp-text {
      margin-top: 8px;
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.4;
      padding: 8px 10px;
      background: var(--bg-surface);
      border-radius: var(--radius-sm);
      border-left: 3px solid var(--teal-primary);
    }

    /* ── PROTOCOL TIMELINE ── */
    .protocol-timeline {
      position: relative;
      padding-left: 32px;
      margin: 20px 0;
    }
    .protocol-timeline::before {
      content: '';
      position: absolute;
      left: 14px;
      top: 10px;
      bottom: 10px;
      width: 2px;
      background: var(--border);
    }
    .timeline-step {
      position: relative;
      margin-bottom: 24px;
    }
    .timeline-step:last-child { margin-bottom: 0; }
    .timeline-badge {
      position: absolute;
      left: -32px;
      top: 0;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--teal-primary);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 700;
      border: 3px solid var(--bg-surface);
      box-shadow: var(--shadow-sm);
    }
    .timeline-content h4 {
      margin: 0 0 6px;
      font-size: 14px;
    }
    .timeline-content p {
      font-size: 12.5px;
      color: var(--text-muted);
      margin: 0;
    }

    /* ── MOBILE RESPONSIVE ── */
    @media (max-width: 840px) {
      .sidebar {
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        transform: translateX(-100%);
        box-shadow: 4px 0 24px rgba(0,0,0,0.4);
      }
      .sidebar.open {
        transform: translateX(0);
      }
      .mobile-menu-btn { display: block; }
      .content-container { padding: 14px; }
      .system-hero { padding: 20px; }
      .cards-subgrid { grid-template-columns: 1fr; }
    }

    /* ── PRINT VIEW ── */
    @media print {
      .sidebar, .top-header, .filter-bar, .expand-icon, .star-btn, .mobile-menu-btn { display: none !important; }
      body { background: #fff !important; color: #000 !important; }
      .content-container { max-width: 100% !important; padding: 0 !important; }
      .topic-card { border: none !important; box-shadow: none !important; page-break-after: always; }
      .card-body { display: block !important; padding: 10px 0 !important; }
      .system-hero { background: #eee !important; color: #000 !important; }
    }
  </style>
</head>
<body>

<div class="app-container">
  <!-- SIDEBAR NAVIGATION -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <div class="app-logo"><i class="fa-solid fa-user-doctor"></i></div>
      <div class="app-title-group">
        <h1>Doctor on Duty</h1>
        <p>System-Wise Clinical Reference</p>
      </div>
    </div>

    <div class="sidebar-system-selector">
      <div class="system-badge"><i class="fa-solid fa-scalpel"></i> Ch. 17: General Surgery</div>
    </div>

    <div class="sidebar-search-box">
      <i class="fa-solid fa-magnifying-glass"></i>
      <input type="text" id="sidebar-search" placeholder="Search 29 topics, drugs, signs...">
    </div>

    <nav class="sidebar-nav" id="sidebar-nav">
      <!-- Populated dynamically via JS -->
    </nav>
  </aside>

  <!-- MAIN WRAPPER -->
  <div class="main-wrapper">
    <!-- TOP CONTROLS HEADER -->
    <header class="top-header">
      <div class="header-left">
        <button class="mobile-menu-btn" id="mobile-toggle"><i class="fa-solid fa-bars"></i></button>
        <div class="header-meta">
          <h2>Chapter 17: General Surgery</h2>
          <span>29 Clinical Topics &bull; Doctor on Duty 3rd Edition (pp. 409–444)</span>
        </div>
      </div>
      <div class="header-actions">
        <button class="btn btn-secondary" id="toggle-all-btn"><i class="fa-solid fa-up-right-and-down-left-from-center"></i> Expand All</button>
        <button class="btn btn-secondary" id="theme-toggle"><i class="fa-solid fa-moon"></i></button>
      </div>
    </header>

    <!-- HORIZONTAL FILTER BAR -->
    <div class="filter-bar" id="filter-bar">
      <div class="filter-pill active" data-cat="all">All Topics <span class="pill-count">29</span></div>
      <div class="filter-pill" data-cat="acute-abdomen">Acute Abdomen <span class="pill-count">5</span></div>
      <div class="filter-pill" data-cat="hpb-pancreas">HPB & Pancreas <span class="pill-count">6</span></div>
      <div class="filter-pill" data-cat="colorectal-anorectal">Colorectal & Anus <span class="pill-count">5</span></div>
      <div class="filter-pill" data-cat="peritonitis">Peritoneal Sepsis <span class="pill-count">2</span></div>
      <div class="filter-pill" data-cat="wounds-ulcers">Wounds & Ulcers <span class="pill-count">2</span></div>
      <div class="filter-pill" data-cat="soft-tissue">Soft Tissue & Minor <span class="pill-count">5</span></div>
      <div class="filter-pill" data-cat="hand-nail">Hand & Nail <span class="pill-count">4</span></div>
      <div class="filter-pill" data-cat="starred"><i class="fa-solid fa-star text-amber"></i> Starred <span class="pill-count" id="starred-pill-count">0</span></div>
    </div>

    <!-- MAIN CONTENT -->
    <main class="content-container">
      <!-- HERO BANNER -->
      <section class="system-hero">
        <span class="hero-badge"><i class="fa-solid fa-book-medical"></i> Doctor on Duty Reference Guide</span>
        <h2>Chapter 17: General Surgery</h2>
        <p>Complete clinical protocol guide comprising all 29 core surgical conditions. Includes diagnostic criteria, Tokyo Guidelines (TG18), Alvarado appendicitis scoring, Ranson/Atlanta pancreatitis stratification, Pakistani and international pharmacotherapy brands, and surgical decision thresholds.</p>
        <div class="hero-meta">
          <span><i class="fa-solid fa-layer-group"></i> <strong>29 Topics Complete</strong></span>
          <span><i class="fa-solid fa-book-open"></i> <strong>Pages 409–444</strong></span>
          <span><i class="fa-solid fa-cloud"></i> <strong>Cloud Sync Active</strong></span>
        </div>
      </section>

      <!-- TOPIC ACCORDION LIST -->
      <div class="topic-list" id="topic-list">
        <!-- TOPICS_PLACEHOLDER -->
      </div>
    </main>
  </div>
</div>

<script>
// --- TOPICS DATA FOR DYNAMIC SEARCH & NAVIGATION ---
const TOPICS_DATA = """ + json.dumps([
  {"num": t["num"], "id": t["id"], "title": t["title"], "category": t["category"], "category_name": t["category_name"], "page": t["book_page"]}
  for t in ALL_TOPICS
]) + """;

document.addEventListener('DOMContentLoaded', () => {
  // --- STARRED / BOOKMARKS STATE (Cloud Sync Compatible) ---
  let starredTopics = JSON.parse(localStorage.getItem('dod_starred') || '[]');

  function saveStarred() {
    localStorage.setItem('dod_starred', JSON.stringify(starredTopics));
    updateStarredUI();
  }

  function toggleStar(num, e) {
    if (e) e.stopPropagation();
    const idx = starredTopics.indexOf(num);
    if (idx > -1) {
      starredTopics.splice(idx, 1);
    } else {
      starredTopics.push(num);
    }
    saveStarred();
  }

  function updateStarredUI() {
    document.querySelectorAll('.star-btn').forEach(btn => {
      const num = parseInt(btn.dataset.num);
      if (starredTopics.includes(num)) {
        btn.classList.add('active');
        btn.innerHTML = '<i class="fa-solid fa-star"></i>';
      } else {
        btn.classList.remove('active');
        btn.innerHTML = '<i class="fa-regular fa-star"></i>';
      }
    });

    document.querySelectorAll('.nav-star').forEach(star => {
      const num = parseInt(star.dataset.num);
      if (starredTopics.includes(num)) {
        star.classList.add('starred');
      } else {
        star.classList.remove('starred');
      }
    });

    document.querySelectorAll('.topic-card').forEach(card => {
      const num = parseInt(card.dataset.num);
      if (starredTopics.includes(num)) {
        card.classList.add('starred-card');
      } else {
        card.classList.remove('starred-card');
      }
    });

    const starCount = document.getElementById('starred-pill-count');
    if (starCount) starCount.textContent = starredTopics.length;
  }

  // --- POPULATE SIDEBAR NAVIGATION ---
  const navEl = document.getElementById('sidebar-nav');
  let currentGroup = '';
  
  TOPICS_DATA.forEach(t => {
    if (t.category_name !== currentGroup) {
      currentGroup = t.category_name;
      const grpTitle = document.createElement('div');
      grpTitle.className = 'nav-group-title';
      grpTitle.textContent = currentGroup;
      navEl.appendChild(grpTitle);
    }

    const item = document.createElement('a');
    item.className = 'nav-item';
    item.href = '#' + t.id;
    item.dataset.num = t.num;
    item.dataset.cat = t.category;
    item.innerHTML = `
      <span class="nav-num">${t.num}</span>
      <span class="nav-title">${t.title}</span>
      <i class="fa-solid fa-star nav-star" data-num="${t.num}"></i>
    `;
    item.addEventListener('click', (e) => {
      // open card and smooth scroll
      const card = document.getElementById(t.id);
      if (card) {
        card.classList.add('open');
        card.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      // close mobile sidebar
      document.getElementById('sidebar').classList.remove('open');
    });
    navEl.appendChild(item);
  });

  // --- TOPIC CARD ACCORDION TOGGLE ---
  document.querySelectorAll('.card-header').forEach(hdr => {
    hdr.addEventListener('click', (e) => {
      if (e.target.closest('.star-btn')) return;
      const card = hdr.closest('.topic-card');
      card.classList.toggle('open');
    });
  });

  // --- STAR BUTTONS CLICK HANDLERS ---
  document.querySelectorAll('.star-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const num = parseInt(btn.dataset.num);
      toggleStar(num, e);
    });
  });

  // --- EXPAND ALL / COLLAPSE ALL ---
  let allExpanded = false;
  const toggleAllBtn = document.getElementById('toggle-all-btn');
  toggleAllBtn.addEventListener('click', () => {
    allExpanded = !allExpanded;
    document.querySelectorAll('.topic-card').forEach(c => {
      if (allExpanded) c.classList.add('open');
      else c.classList.remove('open');
    });
    toggleAllBtn.innerHTML = allExpanded 
      ? '<i class="fa-solid fa-down-left-and-up-right-to-center"></i> Collapse All'
      : '<i class="fa-solid fa-up-right-and-down-left-from-center"></i> Expand All';
  });

  // --- THEME TOGGLE (DARK / LIGHT) ---
  const themeBtn = document.getElementById('theme-toggle');
  const savedTheme = localStorage.getItem('dod_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  themeBtn.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    const nxt = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nxt);
    localStorage.setItem('dod_theme', nxt);
    updateThemeIcon(nxt);
  });

  function updateThemeIcon(t) {
    themeBtn.innerHTML = t === 'dark' ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
  }

  // --- MOBILE SIDEBAR TOGGLE ---
  const mobileToggle = document.getElementById('mobile-toggle');
  const sidebar = document.getElementById('sidebar');
  mobileToggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
  });

  // --- CATEGORY PILL FILTER ---
  let activeCategory = 'all';
  document.querySelectorAll('.filter-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeCategory = pill.dataset.cat;
      filterTopics();
    });
  });

  // --- LIVE SEARCH FILTER ---
  const searchInput = document.getElementById('sidebar-search');
  searchInput.addEventListener('input', () => {
    filterTopics();
  });

  function filterTopics() {
    const q = searchInput.value.trim().toLowerCase();
    
    document.querySelectorAll('.topic-card').forEach(card => {
      const num = parseInt(card.dataset.num);
      const cat = card.dataset.category;
      const text = card.textContent.toLowerCase();
      
      const matchCat = activeCategory === 'all' 
        || (activeCategory === 'starred' && starredTopics.includes(num))
        || (activeCategory === cat);

      const matchSearch = !q || text.includes(q);

      if (matchCat && matchSearch) {
        card.style.display = 'block';
        if (q) card.classList.add('open'); // auto-open on search
      } else {
        card.style.display = 'none';
      }
    });

    // filter sidebar items
    document.querySelectorAll('.nav-item').forEach(item => {
      const num = parseInt(item.dataset.num);
      const cat = item.dataset.cat;
      const text = item.textContent.toLowerCase();

      const matchCat = activeCategory === 'all' 
        || (activeCategory === 'starred' && starredTopics.includes(num))
        || (activeCategory === cat);

      const matchSearch = !q || text.includes(q);

      if (matchCat && matchSearch) {
        item.style.display = 'flex';
      } else {
        item.style.display = 'none';
      }
    });
  }

  // --- INTERACTIVE ALVARADO SCORE CALCULATOR (Topic 6) ---
  const alvCheckboxes = document.querySelectorAll('.alv-check');
  if (alvCheckboxes.length > 0) {
    alvCheckboxes.forEach(chk => {
      chk.addEventListener('change', calculateAlvarado);
    });

    function calculateAlvarado() {
      let score = 0;
      alvCheckboxes.forEach(chk => {
        if (chk.checked) score += parseInt(chk.dataset.pts || '0');
      });

      const scoreBadge = document.getElementById('alv-score');
      const interpText = document.getElementById('alv-interp');
      if (scoreBadge) scoreBadge.textContent = score + ' / 10';

      if (interpText) {
        if (score <= 4) {
          interpText.textContent = `Score ${score} (Low Risk): Appendicitis is unlikely. Outpatient observation or alternate diagnosis workup.`;
          scoreBadge.style.background = '#0d9488';
        } else if (score <= 6) {
          interpText.textContent = `Score ${score} (Intermediate / Compatible): Appendicitis is possible. Inpatient admission, surgical consult & contrast CT recommended.`;
          scoreBadge.style.background = '#d97706';
        } else {
          interpText.textContent = `Score ${score} (High Probability): Acute appendicitis is highly probable (&ge; 7). Urgent surgical exploration indicated!`;
          scoreBadge.style.background = '#e11d48';
        }
      }
    }
  }

  // Initial starred state
  updateStarredUI();
});
</script>

</body>
</html>
"""

# Generate HTML for each topic card
cards_html = []
for t in ALL_TOPICS:
    card = f"""
    <article class="topic-card" id="{t['id']}" data-num="{t['num']}" data-category="{t['category']}">
      <div class="card-header">
        <div class="card-header-left">
          <div class="topic-circle">{t['num']}</div>
          <div class="topic-titles">
            <h3>{t['title']}</h3>
            <div class="topic-badges">
              <span class="badge badge-teal">{t['category_name']}</span>
              <span class="badge badge-amber">{t['badge']}</span>
              <span class="badge badge-page"><i class="fa-solid fa-book"></i> {t['book_page']}</span>
            </div>
          </div>
        </div>
        <div class="card-header-right">
          <button class="star-btn" data-num="{t['num']}" title="Bookmark Topic"><i class="fa-regular fa-star"></i></button>
          <i class="fa-solid fa-chevron-down expand-icon"></i>
        </div>
      </div>
      <div class="card-body">
        <div class="topic-summary-box">
          <i class="fa-solid fa-circle-info"></i> {t['summary']}
        </div>
        {t['content']}
      </div>
    </article>
    """
    cards_html.append(card)

full_html = HTML_TEMPLATE.replace('<!-- TOPICS_PLACEHOLDER -->', '\n'.join(cards_html))

output_path = '/root/doctor-on-duty/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

file_size_kb = os.path.getsize(output_path) / 1024
print(f"Successfully generated {output_path} ({file_size_kb:.2f} KB) with all {len(ALL_TOPICS)} topics!")
