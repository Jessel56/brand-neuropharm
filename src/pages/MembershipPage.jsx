import React from "react";
export default function MembershipPage() {
  return (
    <main className="membership-page">
      <h1>Upgrade Your Membership</h1>
      <p>Unlock advanced courses, labs, and resources with a premium membership.</p>
      <div className="tiers">
        <div className="tier">
          <h2>Student</h2>
          <p>$25/mo</p>
          <button className="stripe-btn">Subscribe with Stripe</button>
        </div>
        <div className="tier">
          <h2>Pro</h2>
          <p>$70/mo</p>
          <button className="stripe-btn">Subscribe with Stripe</button>
        </div>
        <div className="tier">
          <h2>Lab</h2>
          <p>$150/mo</p>
          <button className="stripe-btn">Subscribe with Stripe</button>
        </div>
      </div>
      <p className="note">All payments and personal info are securely handled by Stripe.</p>
    </main>
  );
}
